#
#   Part 1
#

program = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,6,19,23,1,23,5,27,1,27,13,31,2,6,31,35,1,5,35,39,1,39,10,43,2,6,43,47,1,47,5,51,1,51,9,55,2,55,6,59,1,59,10,63,2,63,9,67,1,67,5,71,1,71,5,75,2,75,6,79,1,5,79,83,1,10,83,87,2,13,87,91,1,10,91,95,2,13,95,99,1,99,9,103,1,5,103,107,1,107,10,111,1,111,5,115,1,115,6,119,1,119,10,123,1,123,10,127,2,127,13,131,1,13,131,135,1,135,10,139,2,139,6,143,1,143,9,147,2,147,6,151,1,5,151,155,1,9,155,159,2,159,6,163,1,163,2,167,1,10,167,0,99,2,14,0,0]

for i, val in enumerate(program):
    # Want to iterate over every fourth element in program sequence
    if i % 4 == 0:
        # Break out if code 99, and do it before the rest so we don't
        # try to access array indices that are out of bounds
        if (val == 99):
            break

        index1 = program[i + 1]
        index2 = program[i + 2]
        index3 = program[i + 3]

        if val == 1:
            # For code 1 you should add the values of indicies of the next to positions together
            # and change the value of the third index
            program[index3] = program[index1] + program[index2]
        elif val == 2:
            # For code 1, you should multiply instead
            program[index3] = program[index1] * program[index2]

print "Value at position 0:", program[0]


#
#   Part 2
#

program = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,6,19,23,1,23,5,27,1,27,13,31,2,6,31,35,1,5,35,39,1,39,10,43,2,6,43,47,1,47,5,51,1,51,9,55,2,55,6,59,1,59,10,63,2,63,9,67,1,67,5,71,1,71,5,75,2,75,6,79,1,5,79,83,1,10,83,87,2,13,87,91,1,10,91,95,2,13,95,99,1,99,9,103,1,5,103,107,1,107,10,111,1,111,5,115,1,115,6,119,1,119,10,123,1,123,10,127,2,127,13,131,1,13,131,135,1,135,10,139,2,139,6,143,1,143,9,147,2,147,6,151,1,5,151,155,1,9,155,159,2,159,6,163,1,163,2,167,1,10,167,0,99,2,14,0,0]

for noun in range(0,100):
    for verb in range(0, 100):
        # Make a copy of the original program
        programCopy = program[:]

        programCopy[1] = noun
        programCopy[2] = verb

        for i, val in enumerate(programCopy):
            # Want to iterate over every fourth element in program sequence
            if i % 4 == 0:
                # Break out if code 99, and do it before the rest so we don't
                # try to access array indices that are out of bounds
                if (val == 99):
                    if (programCopy[0] == 19690720):
                        print "noun: ", noun
                        print "verb: ", verb
                        print "Answer: ", 100 * noun + verb
                    break

                index1 = programCopy[i + 1]
                index2 = programCopy[i + 2]
                index3 = programCopy[i + 3]

                if val == 1:
                    # For code 1 you should add the values of indicies of the next to positions together
                    # and change the value of the third index
                    programCopy[index3] = programCopy[index1] + programCopy[index2]
                elif val == 2:
                    # For code 1, you should multiply instead
                    programCopy[index3] = programCopy[index1] * programCopy[index2]
