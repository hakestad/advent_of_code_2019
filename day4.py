puzzle = "137683-596253"

puzzle = puzzle.split("-")
puzzleMin = int(puzzle[0])
puzzleMax = int(puzzle[1])

#
#   Part 1
#
currentValue = puzzleMin
# List to store possible passwords
matches = []
while currentValue < puzzleMax:
    # convert int to string to split up into separate digits and then cast
    # as int again to be able to do arithmetics
    digits = [int(i) for i in str(currentValue)]

    # One criteria for password: two adjacent digits are the same
    if (digits[0] == digits[1] or
        digits[1] == digits[2] or
        digits[2] == digits[3] or
        digits[3] == digits[4] or
        digits[4] == digits[5]):
            # Another criteria for password is that, going from left to right,
            # the values never decrease, they only increase or stay the same
            if (digits[0] <= digits[1] and digits[1] <= digits[2] and
                digits[2] <= digits[3] and digits[3] <= digits[4] and
                digits[4] <= digits[5]):
                matches.append(digits)

    currentValue += 1

print "Length of matches: ", len(matches)

#
#   Part 2 - could probably be optimalized
#

# A more complicated logic is required for this part to find passwords that have
# two adjacent digits that are identical, while not being part of a larger group
# of identical digits
def checkAdjacentDigits(digits, pos):
    maxPos = len(digits) - 1
    # For positions 2 and 3 in out case
    if (pos - 2 >= 0 and pos + 2 <= maxPos):
        if (digits[pos] == digits[pos - 1] and digits[pos] != digits[pos + 1] and digits[pos - 1] != digits[pos - 2]):
            return(True)
        elif (digits[pos] == digits[pos + 1] and digits[pos] != digits[pos - 1] and digits[pos + 1] != digits[pos + 2]):
            return(True)
    # For positions 1 and 4
    elif (pos - 1 >= 0 and pos + 1 <= maxPos):
        if (digits[pos] == digits[pos - 1] and digits[pos] != digits[pos + 1]):
            # Position 4
            if (pos - 2 >= 0):
                if (digits[pos - 1] != digits[pos - 2]):
                    return(True)
        elif (digits[pos] == digits[pos + 1] and digits[pos] != digits[pos - 1]):
            # position 1
            if (pos + 2 <= maxPos):
                if (digits[pos + 1] != digits[pos + 2]):
                    return(True)
    elif (pos + 1 <= maxPos and digits[pos] == digits[pos + 1] and digits[pos + 1] != digits[pos + 2]):
        # Here we don't need to check that pos + 2 is below maxPos, since we
        # know this must be the first position of the list, and there are 5 more
        return(True)
    elif (pos - 1 >= 0 and digits[pos] == digits[pos - 1] and digits[pos - 1] != digits[pos - 2]):
        return(True)
    # If none of the conditions returned True, we return false - conditions were not met
    return False


currentValue = puzzleMin
matches = []
while currentValue < puzzleMax:
    digits = [int(i) for i in str(currentValue)]

    conditionMet = False
    for i in range(0, len(digits)):
        result = checkAdjacentDigits(digits, i)
        if (result == True):
            conditionMet = True

    # If the first condition is met, we can move on to checking the next
    if (conditionMet == True):
        # Another criteria for password is that, going from left to right,
        # the values never decrease, they only increase or stay the same
        if (digits[0] <= digits[1] and digits[1] <= digits[2] and
            digits[2] <= digits[3] and digits[3] <= digits[4] and
            digits[4] <= digits[5]):
            matches.append(digits)

    currentValue += 1

print "Length of matches, second part: ", len(matches)
