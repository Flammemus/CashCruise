import random
import time

def slots(betAmount, balance):
    
    faces = ["-", "+", "x", "7"]
    chosenFaces = []
    gameId = random.randint(1, 100)
    
    if gameId <= 65:
        chosenFaces = random.sample(faces, 3)
    elif gameId <= 80:
        chosenFaces = ["-", "-", "-"]
    elif gameId <= 95:
        chosenFaces = ["+", "+", "+"]
    elif gameId <= 99:
        chosenFaces = ["x", "x", "x"]
    elif gameId <= 100:
        chosenFaces = ["7", "7", "7"]

    print("\nPayout values:\n")
    print("*-------*")
    print("| - - - | 2x")
    print("| + + + | 3x")
    print("| x x x | 5x")
    print("| 7 7 7 | 10x")
    print("*-------*")

    print()
    p = 0.01
    for i in range(40):
        fakeFaces = random.sample(faces, 3)
        print(f"\r| {' '.join(fakeFaces)} |", end="")
        time.sleep(p)
        p = p * 1.1

    print(f"\r| {' '.join(chosenFaces)} |\n", end="")

    if chosenFaces == ["-", "-", "-"]:
        print(f"\n@*- You won {betAmount} schmeckles! -*@")
        return betAmount
    elif chosenFaces == ["+", "+", "+"]:
        print(f"\n@*- You won {betAmount * 2} schmeckles! -*@")
        return betAmount * 2
    elif chosenFaces == ["x", "x", "x"]:
        print(f"\n@*- You won {betAmount * 4} schmeckles! -*@")
        return betAmount * 4
    elif chosenFaces == ["7", "7", "7"]:
        print(f"\n@*- You won {betAmount * 9} schmeckles! -*@")
        return betAmount * 9
    else:
        print(f"\n@*- You lost {betAmount} schmeckles! -*@")
        return -betAmount
    
# slots(50, 500)