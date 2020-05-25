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

def getOrder(coord1, coord2):
    x1, y1, x2, y2 = coord1[0], coord1[1], coord2[0], coord2[1]
    if y1 > y2:
        return 1
    if y1 < y2:
        return 0
    return 1 if x1 > x2 else 0

# Misleading name - doesn't really calculate angle after all, just the ratio
def calculateAngle(coord1, coord2):
    x1, y1, x2, y2 = coord1[0], coord1[1], coord2[0], coord2[1]
    adjacent = x1 - x2
    opposite = y1 - y2

    if adjacent == 0 and opposite > 0:
        return 90
    elif adjacent == 0 and opposite < 0:
        return 270
    elif opposite == 0 and adjacent < 0:
        return 180
    elif opposite == 0 and adjacent > 0:
        return 0
    else:
        return opposite/adjacent

clearPathCounter = [0]*len(astroidCoords)
for i, astroid in enumerate(astroidCoords):
    angles0 = []
    angles1= []
    for target in astroidCoords:
        # Don't check path to self
        if astroid != target:
            # Calculate angle between two astroids and add to angles list
            angle = calculateAngle(astroid, target)
            # calculate if angle is between a target before or after the astroid in question
            order = getOrder(astroid, target)
            angles0.append(angle) if order == 0 else angles1.append(angle)
    # The astroid will have a clear path to only other astroids that don't share
    # angles, so we filter out duplicate angles to see how many astroids are in line of sight
    count1 = len(set(angles0))
    count2 = len(set(angles1))
    clearPathCounter[i] = count1 + count2


mostClearPaths = max(clearPathCounter)
bestAstroidIndex = clearPathCounter.index(mostClearPaths)
bestAstroid = astroidCoords[bestAstroidIndex]
print("The best astroid had a clear view path to: ", mostClearPaths, " other astroids. Position: ", bestAstroid)
