# ==== Can we generate a random number?
import random as rndm

dev = rndm.gauss(0, 1)
print(dev)

# ==== Hey, can we generate a random number from a parameterized distribution? Sorta.

# import random as rndm
# t1 = 4
# if t1 == 5:
#     if rndm.randint(1, 2) == 1:
#         dev = rndm.gauss(-3.5, 3.5)
#     else:
#         dev = rndm.gauss(3.5, 3.5)
# elif t1 > 5 and t1 <= 10:
#     dev = rndm.gauss(-0.5, 2.5)
# elif t1 >= 0 and t1 < 5:
#     dev = rndm.gauss(0.5, 2.5)
#
# print(dev)

# ==== Whoa, can we use that random number to randomly move things around?

# import random as rndm
# from math import floor
# t2 = input("Player 2 - Enter a target integer between 1 to 10 (inclusive): ")
# t2 = int(t2.lower().strip())
# if t2 == 5:
#     if rndm.randint(1, 2) == 1:
#         dev = rndm.gauss(-3.5, 3.5)
#     else:
#         dev = rndm.gauss(3.5, 3.5)
# elif t2 > 5 and t2 <= 10:
#     dev = rndm.gauss(-0.5, 2.5)
# elif t2 >= 0 and t2 < 5:
#     dev = rndm.gauss(0.5, 2.5)
# tgt = floor(t2 + dev)
# if tgt <= 0:
#     score = 0
# elif tgt >= 11:
#     score = 0
# else:
#     score = 10 - abs(tgt - 5)
# print(f"Score: {score}")

# ==== Sweet, can we do that for 2 people?

# ==== Awesome, if we do that for a couple of rounds and keep track of the scores, we can have a game!

