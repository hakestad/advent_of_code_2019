#
#   Part 1
#

totalFuel = 0
with open("day1_puzzle.txt") as puzzle:
    for moduleMass in puzzle:
        # int rounds positive floats down, even if it is closer to round up
        # double int to convert the string moduleMass to number
        totalFuel += int(int(moduleMass)/3) - 2

print "Total fuel:", totalFuel


#
#   Part 2
#
totalFuel = 0
with open("day1_puzzle.txt") as puzzle:
    for moduleMass in puzzle:
        # int rounds positive floats down, even if it is closer to round up
        # double int to convert the string moduleMass to number
        fuelForModule = int(int(moduleMass)/3) - 2
        totalFuel += fuelForModule

        # Calculate the fuel required to carry the fuel needed to carry the module!
        fuelForFuel = int(fuelForModule/3) - 2
        totalFuel += fuelForFuel
        while fuelForFuel > 0:
            fuelForFuel = int(fuelForFuel/3) - 2
            if (fuelForFuel > 0):
                totalFuel += fuelForFuel



print("Total fuel updated:", totalFuel)
