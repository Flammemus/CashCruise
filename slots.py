import random
import time

def slots(betAmount, balance):
    
    faces = ["-", "+", "x", "7"]
    chosenFaces = []
    gameId = random.randint(1, 100)
    
    if gameId <= 55:
        chosenFaces = random.sample(faces, 3)
    
    elif gameId <= 80:
        chosenFaces = ["-", "-", "-"]
    
    elif gameId <= 95:
        chosenFaces = ["+", "+", "+"]
        
    elif gameId <= 99:
        chosenFaces = ["x", "x", "x"]

    elif gameId <= 100:
        chosenFaces = ["7", "7", "7"]

    print()
    p = 0.01
    for i in range(40):
        fakeFaces = random.sample(faces, 3)
        for face in fakeFaces:
            print(face, end=" ")
        time.sleep(p)
        p = p * 1.1

    print("\nChosen Faces:", *chosenFaces)

slots(100, 10000)
