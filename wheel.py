import time
import random

wV = [1, 3, 1, 5, 1, 5, 3, 1, 9, 1, 3, 1, 5, 1, 3, "x", 1, 3, 1, 5, 1, 3, 9]
wwV = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]

def wheel(betAmount, balance):
    print("Wheel time!\n")

    rollTimes = round(random.uniform(3, 4), 2) * 11
    print("- - - - - | - - - - -")

    p = 0.025
    rV = 0
    middleNumbers = []

    for i in range(int(rollTimes)):

        if rV == 23:
            rV = 0

        print("\r" + " ".join(str(wV[(rV + i) % len(wV)]) for i in range(11)), end="")
        middleNumbers.append(wV[(rV + 5) % len(wV)])

        rV = rV + 1

        time.sleep(p)

        p = p * 1.075
        # p = p * 0.0001
    
    print("\nMiddle number:", middleNumbers[-1])
    
    if middleNumbers[-1] == "x":
        print("BONUS!")

wheel(500, 1000)