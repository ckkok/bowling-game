import random
from math import floor


class BowlingGame:
    def __init__(self):
        self.show_banner()
        num_players, num_rounds = self.get_inputs()
        self.max_rounds = num_rounds
        self.num_players = num_players
        self.players = [Player(i) for i in range(1, self.num_players + 1)]

    def show_banner(self):
        print("========================================")
        print("Welcome to Les Terrible Bowling Game!")
        print("Developed by: Kopi Pasta Studios Pte Ltd")
        print("========================================")
        print()

    def get_inputs(self):
        num_players = input("Enter the number of players: ")
        num_players = int(num_players.lower().strip())
        num_rounds = input("Enter the number of rounds to play: ")
        num_rounds = int(num_rounds.lower().strip())
        return num_players, num_rounds

    def calculate_deviation(self, target):
        if target == 5:
            if random.randint(1, 2) == 1:
                deviation = random.gauss(-3.5, 3.5)
            else:
                deviation = random.gauss(3.5, 3.5)
        elif target > 5 and target <= 10:
            deviation = random.gauss(-0.5, 2.5)
        elif target >= 0 and target < 5:
            deviation = random.gauss(0.5, 2.5)
        return deviation

    def calculate_score(self, target):
        deviation = self.calculate_deviation(target)
        actual_target = floor(target + deviation)
        return 10 - abs(actual_target - 5) if actual_target > 0 and actual_target < 11 else 0

    def play_round(self, round):
        print(f"Round {round}!")
        for player in self.players:
            target = player.get_target()
            score = self.calculate_score(target)
            player.increment_score(score)
            player.show_round_score(score)

    def start(self):
        for round in range(1, self.max_rounds + 1):
            self.play_round(round)
        self.end()

    def end(self):
        print("Game over!")
        for player in self.players:
            print(f"Player {player.player_num} scores: {player.score}")


class Player:
    def __init__(self, player_num):
        self.player_num = player_num
        self.score = 0

    def get_target(self):
        target = input(f"Player {self.player_num} - "
                       "Enter a target integer between 1 to 10 (inclusive): ")
        return int(target.lower().strip())

    def increment_score(self, score):
        self.score += score

    def show_round_score(self, score):
        print(f"Player {self.player_num} scores: {score}")


BowlingGame().start()
