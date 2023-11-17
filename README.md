# Les Terrible Bowling Game - A Code Cleaning Exercise

This code simulates a simple bowling game, built by banging out some code as one thinks about it. However, now this dinkly little startup wants to scale and get all enterprisey, so we need new **features**.

## Running the thing

You will need Python 3.9 or JDK >= 11 installed.

To run the Python version, run `python bowling_game.py`. You may need to use `python3` instead of python, depending on your system's configuration.

To run the Java version, run `java BowlingGame.java` if you have Java 11 or later installed.

## Running tests (Python)

Run `pytest test.py`

## Tasks

You should tackle these one at a time sequentially.

- There's a (not so) subtle bug. Player 1 seems to lose the game more often than not. Find it and fix it.
- Extend the game to 10 rounds like, y'know, a proper bowling game.
- Add support for 3 players. A minimum of 2 players is needed for a game, but a 3rd player may be added.
  - What if we wanted to support up to 10 players?

## Stretch Tasks
- Animate the game in the console
