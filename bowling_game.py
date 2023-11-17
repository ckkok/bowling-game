import random as rndm
from math import floor

print("========================================")
print("Welcome to Les Terrible Bowling Game!")
print("Developed by: Kopi Pasta Studios Pte Ltd")
print("========================================")
print()

rnd = 1

s1 = 0
s2 = 0

laneFlag = True

while True:
    print(f"Round {rnd}!")
    t1 = input("Player 1 - Enter a target integer between 1 to 10 (inclusive): ")
    t1 = int(t1.lower().strip())
    if t1 == 5:
        if rndm.randint(1, 2) == 1:
            if not laneFlag:
                dev = rndm.gauss(-3.5, 3.5)
            else:
                dev = rndm.gauss(-4.5, 5.5)
        else:
            if not laneFlag:
                dev = rndm.gauss(3.5, 3.5)
            else:
                dev = rndm.gauss(4.5, 5.5)
    elif t1 > 5 and t1 <= 10:
        dev = rndm.gauss(-0.5, 2.5)
    elif t1 >= 0 and t1 < 5:
        dev = rndm.gauss(0.5, 2.5)
    tgt = floor(t1 + dev)
    if tgt <= 0:
        score = 0
    elif tgt >= 11:
        score = 0
    else:
        score = 10 - abs(tgt - 5)
    print(f"Player 1 scores: {score}")
    s1 = s1 + score
    t2 = input("Player 2 - Enter a target integer between 1 to 10 (inclusive): ")
    t2 = int(t2.lower().strip())
    if t2 == 5:
        if rndm.randint(1, 2) == 1:
            dev = rndm.gauss(-3.5, 3.5)
        else:
            dev = rndm.gauss(3.5, 3.5)
    elif t2 > 5 and t2 <= 10:
        dev = rndm.gauss(-0.5, 2.5)
    elif t2 >= 0 and t2 < 5:
        dev = rndm.gauss(0.5, 2.5)
    tgt = floor(t2 + dev)
    if tgt <= 0:
        score = 0
    elif tgt >= 11:
        score = 0
    else:
        score = 10 - abs(tgt - 5)
    print(f"Player 2 scores: {score}")
    s2 = s2 + score
    rnd = rnd + 1
    if rnd > 5:
        break

print("Game over!")
if s1 > s2:
    print(f"Player 1 wins! Score {s1} to {s2}")
else:
    print(f"Player 2 wins! Score {s2} to {s1}")
