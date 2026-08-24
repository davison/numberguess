import os
import unittest
from unittest.mock import patch

from numberguess import play_game, supports_terminal_style


class NumberGuessTests(unittest.TestCase):
    def run_game(self, guesses, secret=50, styled=False):
        supplied_guesses = iter(guesses)
        prompts = []
        output = []
        picker_calls = []

        def input_fn(prompt):
            prompts.append(prompt)
            return next(supplied_guesses)

        def secret_picker(minimum, maximum):
            picker_calls.append((minimum, maximum))
            return secret

        attempts = play_game(input_fn, output.append, secret_picker, styled=styled)
        return attempts, prompts, output, picker_calls

    def test_selects_secret_from_inclusive_game_range_and_prompts(self):
        attempts, prompts, output, picker_calls = self.run_game(["50"])

        self.assertEqual([(1, 100)], picker_calls)
        self.assertEqual(["Enter your guess: "], prompts)
        self.assertEqual("I'm thinking of a number from 1 to 100.", output[0])
        self.assertEqual(1, attempts)

    def test_reports_low_and_high_guesses_before_success(self):
        attempts, prompts, output, _ = self.run_game(["25", "75", "50"])

        self.assertEqual(3, attempts)
        self.assertEqual(3, len(prompts))
        self.assertIn("Too low.", output)
        self.assertIn("Too high.", output)
        self.assertEqual("Correct! You guessed the number in 3 attempts.", output[-1])

    def test_invalid_and_out_of_range_input_do_not_count(self):
        attempts, prompts, output, _ = self.run_game(
            ["not a number", "0", "101", "50"]
        )

        self.assertEqual(1, attempts)
        self.assertEqual(4, len(prompts))
        self.assertIn("Please enter a whole number.", output)
        self.assertEqual(
            2, output.count("Please enter a number from 1 to 100.")
        )
        self.assertEqual("Correct! You guessed the number in 1 attempt.", output[-1])

    def test_game_exits_immediately_after_correct_guess(self):
        attempts, prompts, output, _ = self.run_game(["50", "25"])

        self.assertEqual(1, attempts)
        self.assertEqual(1, len(prompts))
        self.assertEqual("Correct! You guessed the number in 1 attempt.", output[-1])

    def test_styled_game_decorates_each_kind_of_feedback(self):
        attempts, prompts, output, _ = self.run_game(
            ["nope", "0", "25", "75", "50"], styled=True
        )

        rendered = "\n".join(prompts + output)
        self.assertEqual(3, attempts)
        self.assertIn("\033[", rendered)
        for icon in ("🎯", "➜", "⚠", "↑", "↓", "🎉"):
            self.assertIn(icon, rendered)
        self.assertIn("NUMBER GUESS", output[0])
        self.assertTrue(output[-1].endswith("\033[0m"))

    def test_injected_io_defaults_to_plain_output(self):
        _, prompts, output, _ = self.run_game(["50"], styled=None)

        rendered = "".join(prompts + output)
        self.assertNotIn("\033[", rendered)
        self.assertNotIn("🎯", rendered)


class TerminalStyleSupportTests(unittest.TestCase):
    class FakeStream:
        def __init__(self, interactive, encoding="utf-8"):
            self.interactive = interactive
            self.encoding = encoding

        def isatty(self):
            return self.interactive

    def test_supports_style_in_an_interactive_terminal(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertTrue(supports_terminal_style(self.FakeStream(True)))

    def test_disables_style_for_redirected_output(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(supports_terminal_style(self.FakeStream(False)))

    def test_disables_style_when_stream_cannot_encode_icons(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(
                supports_terminal_style(self.FakeStream(True, encoding="ascii"))
            )

    def test_respects_no_color_and_dumb_terminal_conventions(self):
        stream = self.FakeStream(True)

        with patch.dict(os.environ, {"NO_COLOR": "1"}, clear=True):
            self.assertFalse(supports_terminal_style(stream))
        with patch.dict(os.environ, {"TERM": "dumb"}, clear=True):
            self.assertFalse(supports_terminal_style(stream))


if __name__ == "__main__":
    unittest.main()
