#
#   Part 1 & 2 combined
#

program = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,82,10,225,101,94,44,224,101,-165,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1102,35,77,225,1102,28,71,225,1102,16,36,225,102,51,196,224,101,-3468,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1001,48,21,224,101,-57,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,2,188,40,224,1001,224,-5390,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1101,9,32,224,101,-41,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1102,66,70,225,1002,191,28,224,101,-868,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,1,14,140,224,101,-80,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1102,79,70,225,1101,31,65,225,1101,11,68,225,1102,20,32,224,101,-640,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,226,224,1002,223,2,223,1006,224,329,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,344,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,359,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,374,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,389,1001,223,1,223,7,677,226,224,1002,223,2,223,1006,224,404,101,1,223,223,7,226,226,224,1002,223,2,223,1005,224,419,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,7,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,464,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,479,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,509,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1007,677,226,224,102,2,223,223,1005,224,539,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,554,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,569,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,584,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,614,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,629,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,644,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,659,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]

opCode = 0
pointer = 0
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
        # Take single input value and store that value at the position given by parameter
        try:
            val = int(input("Input: "))
        except ValueError:
            print "Not a number."

        program[index1] = val
        # Increase pointer by 2, since this instruction has only one parameter
        pointer += 2
    elif opCode == 4:
        # Output value at the position given by the first parameter, or the index value if mode == 1
        out = program[index1] if mode1 == 0 else index1
        print "Output: ", out
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
