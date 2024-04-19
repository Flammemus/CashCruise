import random
import time

def roulette(betAmount, balance):

    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    everySlot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    winningBet = random.choice(everySlot)

    print("Choose what group to bet on:\n")
    print("1. single number")
    print("2. color\n")

    action = input(": ")

    if action.lower() == "1":
        print("Bet on any number from 1 to 36")
        action = input(": ")

    print(winningBet)