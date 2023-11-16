# Les Terrible Bowling Game - A Code Cleaning Exercise

This code simulates a simple bowling game, built by banging out some code as one thinks about it. However, now this dinkly little startup wants to scale and get all enterprisey, so we need new **features**.

## Running the thing

You will need Python 3.9 or JDK >= 11 installed.

To run the Python version, run `python bowling_game.py`. You may need to use `python3` instead of python, depending on your system's configuration.

To run the Java version, run `java BowlingGame.java` if you have Java 11 or later installed.

## Tasks

You should tackle these one at a time sequentially.

- There's a (not so) subtle bug. Player 1 seems to lose the game more often than not. Find it and fix it.
- Extend the game to 10 rounds like, y'know, a proper bowling game.
- Add support for a 3rd player
- A player may be good or terrible, and the bowling balls used may be good or lousy. The bowling ball is selected by the player randomly before making a throw. A good player using a good ball should have a deviation from his target lowered by 1.5. A terrible player using a lousy ball should have a deviation from his target increased by 1.5. However, a good player using a lousy ball should have his deviation increased by 0.5 and randomly insult the ball (print it out). A terrible player using a good ball should have his deviation unchanged.
- In a terrible bowling venue, not all lanes are created equal. Maybe the janitor forgot to clean some lanes. Add a random chance that a player ends up bowling on a lousy lane, bearing in mind that players may bowl on different lanes on different turns.
- Add support for up to 10 players. Do not read this before the 3rd task.

## Stretch Tasks
- Animate the game in the console
