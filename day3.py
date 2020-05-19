#
#   Part 1 & 2 combined
#
paths = []
with open("day3_puzzle.txt") as puzzle:
    for i, path in enumerate(puzzle):
        paths.append(path.split(","))

path1 = paths[0]
path2 = paths[1]
# Representing coordinates as strings for easier intersection comparison later
# For part 2: The last digit represents steps taken to get to each coord
wire1 = ["0,0,0"]
wire2 = ["0,0,0"]

def move(instruction, currPos):
    # Extract info from instruction - composed of letter representing direction
    # and the number of steps that are to be taken in that direction
    dir = instruction[:1]
    steps = int(instruction[1:])

    currPos = currPos.split(",")
    currentX = int(currPos[0])
    currentY = int(currPos[1])
    # For part 2: keep track of steps taken
    currentSteps = int(currPos[2])

    moves = []
    for i in range(0, steps):
        if (dir == 'R'):
            currentX += 1
        elif (dir == 'L'):
            currentX -= 1
        elif (dir == 'U'):
            currentY += 1
        elif (dir == 'D'):
            currentY -= 1
        # increment steps
        currentSteps += 1
        # Backtick to concatenate string and int
        moves.append(`currentX` + "," + `currentY` + "," + `currentSteps`)
    return(moves)


for i, instruction in enumerate(path1):
    # Append new coordinates after each instruction
    wire1 += move(instruction, wire1[len(wire1) - 1])

for i, instruction in enumerate(path2):
    wire2 += move(instruction, wire2[len(wire2) - 1])

# To compare just x and y coordinates for the two wires to find intersections,
# we need to make a copy of the two wires where we strip the number of steps
# taken (the last part of the string, after the second comma)
trimmed1 = [','.join(coord.split(",")[0:2]) for coord in wire1]
trimmed2 = [','.join(coord.split(",")[0:2]) for coord in wire2]

# To keep the indice of where it intersects, convert to dictionnary
dict1 = dict((k,val) for val,k in enumerate(trimmed1))
dict2 = dict((k,val) for val,k in enumerate(trimmed2))

# Find all values in the two dictionnaries that are identical
intersects = set(dict1).intersection(dict2)

# Don't count the starting point, where the two wires cross by default
intersects.remove("0,0")

distances = []
sumSteps = []
for val in intersects:
    valArr = val.split(",")
    # Add absolute value of x and y for each intersecting coordinate to
    # calculate manhattan distance
    manhattanDist = abs(int(valArr[0])) + abs(int(valArr[1]))
    distances.append(manhattanDist)

    # Get indices for the positions matching the value of the intersect
    ind1 = dict1[val]
    ind2 = dict2[val]
    # Get the full entry fir each wire, so that we can acces steps taken for each intersect
    selected1 = wire1[ind1]
    selected2 = wire2[ind2]
    # split the coords so that we can sum up the steps
    coords1 = selected1.split(",")
    coords2 = selected2.split(",")
    sumSteps.append(int(coords1[2]) + int(coords2[2]))

# Find the smallest value for both puzzles
distances.sort()
sumSteps.sort()
# Print smallest manhattan distance
print("Manhattan distance: ", distances[0]) # <---- solution to first part
# Print smallest sum of steps
print("Smallest sum of steps: ", sumSteps[0]) # <----- solution to second part
