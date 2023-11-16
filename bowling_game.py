import random
from math import floor

print("========================================")
print("Welcome to Les Terrible Bowling Game!")
print("Developed by: Kopi Pasta Studios Pte Ltd")
print("========================================")
print()

round = 1

player_1_score = 0
player_2_score = 0

is_lousy_lane = True

while True:
    print(f"Round {round}!")
    player_1_target = input("Player 1 - Enter a target integer between 1 to 10 (inclusive): ")
    player_1_target = int(player_1_target.lower().strip())
    if player_1_target == 5:
        if random.randint(1, 2) == 1:
            if not is_lousy_lane:
                deviation = random.gauss(-3.5, 3.5)
            else:
                deviation = random.gauss(-4.5, 5.5)
        else:
            if not is_lousy_lane:
                deviation = random.gauss(3.5, 3.5)
            else:
                deviation = random.gauss(4.5, 5.5)
    elif player_1_target > 5 and player_1_target <= 10:
        deviation = random.gauss(-0.5, 2.5)
    elif player_1_target >= 0 and player_1_target < 5:
        deviation = random.gauss(0.5, 2.5)
    actual_target = floor(player_1_target + deviation)
    if actual_target <= 0:
        score = 0
    elif actual_target >= 11:
        score = 0
    else:
        score = 10 - abs(actual_target - 5)
    print(f"Player 1 scores: {score}")
    player_1_score = player_1_score + score
    player_2_target = input("Player 2 - Enter a target integer between 1 to 10 (inclusive): ")
    player_2_target = int(player_2_target.lower().strip())
    if player_2_target == 5:
        if random.randint(1, 2) == 1:
            deviation = random.gauss(-3.5, 3.5)
        else:
            deviation = random.gauss(3.5, 3.5)
    elif player_2_target > 5 and player_2_target <= 10:
        deviation = random.gauss(-0.5, 2.5)
    elif player_2_target >= 0 and player_2_target < 5:
        deviation = random.gauss(0.5, 2.5)
    actual_target = floor(player_2_target + deviation)
    if actual_target <= 0:
        score = 0
    elif actual_target >= 11:
        score = 0
    else:
        score = 10 - abs(actual_target - 5)
    print(f"Player 2 scores: {score}")
    player_2_score = player_2_score + score
    round = round + 1
    if round > 5:
        break

print("Game over!")
if player_1_score > player_2_score:
    print(f"Player 1 wins! Score {player_1_score} to {player_2_score}")
else:
    print(f"Player 2 wins! Score {player_2_score} to {player_1_score}")
