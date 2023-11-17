import io
import sys
from unittest import TestCase, mock


@mock.patch('random.gauss', create=True)
@mock.patch('random.randint', create=True)
@mock.patch('builtins.input', create=True)
class BowlingGameTest(TestCase):
    def test_game(self, mocked_input, mocked_randint, mocked_gauss):
        self.maxDiff = None
        mocked_input.side_effect = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        mocked_randint.side_effect = [1, 1, 1, 1, 2, 1, 1, 1, 1, 1]  # Which side to push the ball from the center when input is 5
        mocked_gauss.side_effect = [0.5, 1.0, 0.0, 1.5, 4.5, -0.5, -1.0, 0.0, -1.5, 0.5]  # The deviation to apply
        captured_output = io.StringIO()
        sys.stdout = captured_output
        import random
        random.seed(0)
        import bowling_game
        expected_output = """========================================
Welcome to Les Terrible Bowling Game!
Developed by: Kopi Pasta Studios Pte Ltd
========================================

Round 1!
Player 1 scores: 6
Player 2 scores: 8
Round 2!
Player 1 scores: 8
Player 2 scores: 10
Round 3!
Player 1 scores: 6
Player 2 scores: 10
Round 4!
Player 1 scores: 9
Player 2 scores: 7
Round 5!
Player 1 scores: 8
Player 2 scores: 5
Game over!
Player 2 wins! Score 40 to 37
"""
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)
