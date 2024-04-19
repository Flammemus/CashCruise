import random
import time

def coinflip(betAmount, balance):

    betChoices = ["h", "t"]

    print("\nBet on heads or tails? (h/t): \n")
    action = input(": ")

    result = random.choice(betChoices)

    def printHeads():
        print("\r| Heads |", end="")

    def printTails():
        print("\r| Tails |", end="")

    while True:

        print()
        p = 0.3
        for i in range(8):
            printHeads()
            time.sleep(p)
            p = p / 1.2
            printTails()
            time.sleep(p)
            p = p / 1.2

        if result == "h":
            printHeads()
            print("\r")
        else:
            printTails()
            print("\r")

        time.sleep(0.5)

        if action.lower() not in betChoices:
            print("\nInvalid choice, try again\n")

        if action.lower() == result:
            print(f"\n@*- You won {betAmount}! -*@")
            return betAmount
        if action.lower() != result:
            print(f"\n@*- You lost {betAmount}! -*@")
            return -betAmount