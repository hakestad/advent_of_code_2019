# Import class Intcode that was re-written from day 2 and day 5
from intcode import Intcode
# Using a library for permutations
import itertools

program = [3,8,1001,8,10,8,105,1,0,0,21,30,55,80,101,118,199,280,361,442,99999,3,9,101,4,9,9,4,9,99,3,9,101,4,9,9,1002,9,4,9,101,4,9,9,1002,9,5,9,1001,9,2,9,4,9,99,3,9,101,5,9,9,1002,9,2,9,101,3,9,9,102,4,9,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,102,3,9,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99]


#
#   Part 1
#

# Setup all the possible unique permutations of the values 0 to 4
# --- UPDATE: Found a shorter solution -- see part 2
phaseSequences = [seq for seq in list(itertools.product(range(5), repeat=5)) if len(set(seq)) == 5]

outputList = []

for seq in phaseSequences:
    amps = []
    output = 0
    for i in range(0,5):
        # Initialize each apmlifier with a copy of the program code (Python uses
        # pass by object reference, but in the class, we setup a new variable
        # self.program, so it doens't point to the same object in memory anymore.
        # Or so I've understood it.)
        # and their own phase for this sequence. Pointer should be 0
        amps.append(Intcode(program, seq[i], 0))
        # As long as the current amp hasn't run its course yet, we wait
        while(amps[i].getCode() != 99):
            out = amps[i].run(output)
            # The break statement counts as a None value, and we
            # don't save that, because else the output sent to next amp is None
            if out != None:
                output = out
        # Save the final output from this sequence so we can compare which
        # sequence did best (highest output) at the end
        outputList.append(output)

highestOutput = max(outputList)
highestOutputIndex = outputList.index(highestOutput)

print "----------------------------------------------------------------------"
print "Highest output for part 1 was: ", highestOutput, " and the sequence was: ", phaseSequences[highestOutputIndex]
print "----------------------------------------------------------------------"

#
#   Part 2
#

# Found a shorter way of generating permutations in itertools
phaseSequences = list(itertools.permutations(range(5, 10)))

outputList = []
for seq in phaseSequences:
    amps = []
    for i in range(0,5):
        # each amp starts with a fresh copy of the program -- see comment in part 1
        # so no need to do program[:]
        amps.append(Intcode(program, seq[i], 0))
    output = 0

    while(amps[4].getCode() != 99):
        # Here we need the amps to not run until completed, we want a loop where
        # the first output of the first amp is sent to the second amp and so forth,
        # for many rounds to generate a larger output, instead of the last output
        output = amps[4].run(amps[3].run(amps[2].run(amps[1].run(amps[0].run(output)))))
        outputList.append(output)

print "Highest output for part 2 was: ", max(outputList)
print "----------------------------------------------------------------------"
