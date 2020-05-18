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
    currentSteps += steps

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
# taken (the last two characters in the string)
trimmed1 = [','.join(coord.split(",")[0:2]) for coord in wire1]
trimmed2 = [','.join(coord.split(",")[0:2]) for coord in wire2]

# To keep the indice of where it intersects, convert to dictionnary
dict1 = dict((k,i) for i,k in enumerate(trimmed1))
dict2 = dict((k,i) for i,k in enumerate(trimmed2))

# Find all values in the two lists that are identical
intersects = set(dict1).intersection(dict2)

# make copy of intersect to be used in part 2
intersectsCopy = intersects.copy()

# Don't count the starting point, where the two wires cross by default
intersects.remove("0,0")

distances = []
indices = []
for val in intersects:
    val = val.split(",")
    # Add absolute value of x and y for each intersecting coordinate to
    # calculate manhattan distance
    manhattanDist = abs(int(val[0])) + abs(int(val[1]))
    distances.append(manhattanDist)

distances.sort()
# Print smallest manhattan distance
print(distances[0]) # <---- solution to first part

#
#   Part 2
#
print(intersectsCopy)
# Get the indices for the two wires where they intersect
indices1 = [dict1[x] for x in intersectsCopy]
indices2 = [dict2[x] for x in intersectsCopy]
print(indices1)
sumSteps = []
for i in range(0, len(intersectsCopy)):
    coords1 = wire1[indices1[i]].split(",")
    coords2 = wire2[indices2[i]].split(",")

    print(coords1)
    print(coords2)
    #steps1 = wire1[indices1[i]].split(",")[2]
    #steps2 = wire2[indices2[i]].split(",")[2]
    #sumSteps.append(int(steps1) + int(steps2))

#sumSteps.sort()
# Print the lowest number of steps needed to be taken by the two wires together
# to reach an intersection
#print(sumSteps[0])
