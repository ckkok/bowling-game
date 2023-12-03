# Les Terrible Bowling Game - A Code Cleaning Exercise

This code simulates a simple bowling game, built by banging out some code as one thinks about it. However, now this dinkly little startup wants to scale and get all enterprisey, so we need new **features**.

## Features!

Everybody loves features.

1. When someone runs our programme, we will print the following banner, including the trailing line as whitespace separating the banner from the actual game.
========================================
Welcome to Les Terrible Bowling Game!
Developed by: Kopi Pasta Studios Pte Ltd
========================================

2. Announce the round number loudly by printing "Round (number)!"

3. Get the first player to enter a target integer between 1 and 10 (inclusive).
   If the player's target is 5, add or subtract a random decimal from it. If the lane is considered lousy, the random decimal should be larger on average.
   If the target is more than 5, subtract a random decimal from it.
   If the target is less than 5, add a random decimal to it.
   Take the largest integer less than the adjusted target as the actual target.
   The player's score is then 10 - (distance of the actual target away from 5), so that if the actual target is 5, he should get the maximum 10 points.
   Note that he should score 0 if his actual target is outside of the bounds.
   Then, we announce his score with "Player 1 scores: (his score)".

4. Get the second player to enter a target integer between 1 and 10 (inclusive).
   Calculate his score and announce it in the same way as we did for player 1.

5. Repeat steps 3 and 4 for another 4 rounds, so that the game lasts for a total of 5 rounds.

6. Loudly announce the game to be over by printing "Game over!"

7. If player 1 wins, announce it by printing "Player 1 wins! Score (player 1 score) to (player 2 score)".
   If player 2 wins, announce it by printing "Player 2 wins! Score (player 2 score) to (player 1 score)" instead.

## Running the thing

You will need Python >= 3.9 or JDK >= 11 installed to run the respective language variations.

To run the Python version, run `python bowling_game.py`. You may need to use `python3` instead of python, depending on your system's configuration.

To run the Java version, run `java BowlingGame.java` if you have Java 11 or later installed.

## Running tests (Python)

Run `pytest test.py`. Since the test intercepts user input prompts to inject static pre-defined inputs, you will not see such prompts.

## Tasks

You should tackle these one at a time sequentially.

- There's a (not so) subtle bug. Player 1 seems to lose the game more often than not. Find it and fix it.
- Extend the game to 10 rounds like, y'know, a proper bowling game.
- Add support for 3 players. A minimum of 2 players is needed for a game, but a 3rd player may be added.
  - What if we wanted to support up to 10 players?

## Stretch Tasks
- Animate the game in the console
