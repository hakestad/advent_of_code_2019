#
#   Reusing part of code from day 5
#

# @program  - List. Program to run
# @outputList - List. Stores the outputs from the program
# @inputType - String. defaults to user input, but can be set to "program" which
#   means it will read from a list provided as either the phase or the outputList
#   depending on an internal state
# @phase - Int. used by day7. Will be the phase for one run of the program
def intcode(program, output, inputType = "user", phase = 0):
    opCode = 0
    pointer = 0

    # internal state that decided whether to use phase as "input" or last item in outputList as "input"
    useInputPhase = True

    while opCode != 99:

        codes = [int(i) for i in str(program[pointer])]
        numCodes = len(codes)

        # The opCode is the two rightmost digits of the instruction, or the last digit for instructions
        # that are lacking modes and are only single digit - handle this with ternary construct
        # Need to combine them to a string to put them together, then re-convert back to int
        opCode = int(`codes[numCodes - 2]` + `codes[numCodes - 1]`) if numCodes >= 2 else codes[0]

        if opCode == 99:
            break

        # Defaults are mode 0 - position mode, else read mode from
        # third last, fourth last or fifth last code if they exist
        mode1 = codes[numCodes - 3] if numCodes >= 3 else 0
        mode2 = codes[numCodes - 4] if numCodes >= 4 else 0
        mode3 = codes[numCodes - 5] if numCodes >= 5 else 0

        index1 = program[pointer + 1]
        # Only setup indices for these if there are appropriate number of params for this opCode
        index2 = program[pointer + 2] if opCode == 1 or opCode == 2 or opCode == 5 or opCode == 6 or opCode == 7 or opCode == 8 else None
        index3 = program[pointer + 3] if opCode == 1 or opCode == 2 or opCode == 7 or opCode == 8 else None

        if opCode == 1:
            # Depending on the mode, you should either add the values at
            # the indexed positions (mode == 0) together, or add the
            # direct values (indices) together (mode == 1)
            a1 = program[index1] if mode1 == 0 else index1
            a2 = program[index2] if mode2 == 0 else index2

            program[index3] = a1 + a2
            # Increase pointer by 4, since this instruction uses three parameters
            pointer += 4
        elif opCode == 2:
            # For code 2, you should multiply instead
            m1 = program[index1] if mode1 == 0 else index1
            m2 = program[index2] if mode2 == 0 else index2
            program[index3] = m1 * m2
            # Increase pointer by 4, since this instruction uses three parameters
            pointer += 4
        elif opCode == 3:
            val = 0

            if inputType == 'user':
                # Take single input value and store that value at the position given by parameter
                try:
                    val = int(input("Input: "))
                except ValueError:
                    print "Not a number."
            else:
                if useInputPhase == True:
                    val = phase
                    # Set to false so that it uses last item in outputList next time
                    useInputPhase = False
                else:
                    # If not, it means the last output passed in should be used
                    val = output
                    #print "VAL: ", val

            program[index1] = val
            # Increase pointer by 2, since this instruction has only one parameter
            pointer += 2
        elif opCode == 4:
            # Output value at the position given by the first parameter, or the index value if mode == 1
            output = program[index1] if mode1 == 0 else index1
            #print "Output: ", output

            # Increase pointer by 2, since this instruction has only one parameter
            pointer += 2
        elif opCode == 5:
            firstParam = program[index1] if mode1 == 0 else index1
            if (firstParam != 0):
                pointer = program[index2] if mode2 == 0 else index2
            else:
                pointer += 3
        elif opCode == 6:
            firstParam = program[index1] if mode1 == 0 else index1
            if (firstParam == 0):
                pointer = program[index2] if mode2 == 0 else index2
            else:
                pointer += 3
        elif opCode == 7:
            firstParam = program[index1] if mode1 == 0 else index1
            secondParam = program[index2] if mode2 == 0 else index2
            program[index3] = 1 if firstParam < secondParam else 0
            pointer += 4
        elif opCode == 8:
            firstParam = program[index1] if mode1 == 0 else index1
            secondParam = program[index2] if mode2 == 0 else index2
            program[index3] = 1 if firstParam == secondParam else 0
            pointer += 4
    return output


def amplifierOutputChecker(program, phaseSequences, outputList):

    for seq in phaseSequences:
        print "sequence: ", seq
        # For each sequence, we reset the temporary list of outputs
        output = 0
        for phase in seq:
            # Each amplifier will have its own program
            testProgram = program[:]
            print "phase", phase
            output = intcode(testProgram, output, "program", phase)
        # Save the last output to store to be able to compare
        # which sequence yielded the highest output
        outputList.append(output)
    print outputList
    return outputList
