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

#
#   Part 2 - Complete vaporization by giant laser
#
def calcDistance(coord1, coord2):
    x1, y1, x2, y2 = coord1[0], coord1[1], coord2[0], coord2[1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def splitDictionary(dict):
    first = {x: dict[x] for x in dict if x >= 90.0}
    last = {x: dict[x] for x in dict if x < 90}
    return first, last

def findAstroidToVaporize(astroids, monitoringStation):
    # In case only one astroid in array, then that one is the one to be vaporized
    astroidToVaporize = astroids[0]
    # But if there are more, we calculate which is closest to our monitoring station
    if len(astroids) > 1:
        currentDist = calcDistance(monitoringStation, astroidToVaporize)
        for astroid in astroids[1:]:
            # Find the closest astroid at this angle
            dist = calcDistance(monitoringStation, astroid)
            if dist < currentDist:
                currentDist = dist
                astroidToVaporize = astroid
    return astroidToVaporize


# Setup the monitoring station at the location of the astroid with the best view
monitoringStation = bestAstroid

vaporized = []
# AstroidCoords need to be above 1, because 1 is our monitoring station
while len(astroidCoords) > 1:
    astroidsPerAngle = {}
    for target in astroidCoords:
        # Don't check self
        if monitoringStation != target:
            angle = calculateAngle(monitoringStation, target)
            if angle not in astroidsPerAngle:
                astroidsPerAngle[angle] = []
            astroidsPerAngle[angle].append(target)

    # A bit hacky, need to start at degrees = 90 and go through the angles sorted
    firstAstroidsPerAngle, lastAstroidsPerAngle = splitDictionary(astroidsPerAngle)

    astroidsToVaporize = []
    # Start at angle = 90 and go clockwise
    for angle in sorted(firstAstroidsPerAngle):
        astroids = firstAstroidsPerAngle[angle]
        astroidsToVaporize.append(findAstroidToVaporize(astroids, monitoringStation))
    # Then go over angles from 0 to 90 (fourth quadrant)
    for angle in sorted(lastAstroidsPerAngle):
        astroids = lastAstroidsPerAngle[angle]
        astroidsToVaporize.append(findAstroidToVaporize(astroids, monitoringStation))

    vaporized.extend(astroidsToVaporize)
    astroidCoords = [a for a in astroidCoords if a not in astroidsToVaporize]

print(vaporized[199])
print("Answer to part 2: ", vaporized[199][0] * 100 + vaporized[199][1])
