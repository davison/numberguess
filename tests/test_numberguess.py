import unittest

from numberguess import play_game


class NumberGuessTests(unittest.TestCase):
    def run_game(self, guesses, secret=50):
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

        attempts = play_game(input_fn, output.append, secret_picker)
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


if __name__ == "__main__":
    unittest.main()
