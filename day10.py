import math
import numpy as np
#
#   Part 1
#
astroidCoords = []
with open("day10_puzzle.txt") as puzzle:
    for i, row in enumerate(puzzle):
        row = list(row)
        for j, col in enumerate(row):
            if col == '#':
                # flip coords around to make them match the expected format of the puzzle
                astroidCoords.append([j, i])

def calculateAngle(coord1, coord2):
    x1, y1, x2, y2 = coord1[0], coord1[1], coord2[0], coord2[1]
    # Using the arctan2 function to calculate the whole unit circle
    # multiplying and dividing by pi/180 to convert to degrees from radians
    angle = np.arctan2(y2-y1, x2-x1) * 180 / math.pi + 180
    return angle

clearPathCounter = [0]*len(astroidCoords)
for i, astroid in enumerate(astroidCoords):
    angles = []
    for target in astroidCoords:
        # Don't check path to self
        if astroid != target:
            # Calculate angle between two astroids and add to angles list
            angles.append(calculateAngle(astroid, target))
    # The astroid will have a clear path to only other astroids that don't share
    # angles, so we filter out duplicate angles to see how many astroids are in line of sight
    clearPathCounter[i] = len(set(angles))


mostClearPaths = max(clearPathCounter)
bestAstroidIndex = clearPathCounter.index(mostClearPaths)
bestAstroid = astroidCoords[bestAstroidIndex]
print("The best astroid had a clear view path to: ", mostClearPaths, " other astroids. Position: ", bestAstroid)
