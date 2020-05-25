#
#   Starting afresh, because the code from day 2 and 5 was kinda bad
#   Going for a better structure here, using an object oriented approach
#   for easier control of each Intcode object's state
#

class Intcode:
    # @testMode lets user input value from keyboard during testing
    def __init__(self, program, phase, pointer, testMode = False):
        self.phase = phase
        self.pointer = pointer
        self.program = program
        # extend program with much larger memory
        self.program.extend([0]*1000)
        self.code = 0
        self.relativeBase = 0
        self.testMode = testMode
        # For the first input, we use the value of the phase
        # else we take the inputValue supplied in the run function
        # This Boolean keeps track of the input state
        self.initialInput = True

    def getCode(self):
        return self.code

    def getModes(self, codes, numCodes):
        # Defaults are mode 0 - position mode, else read mode from
        # third last, fourth last or fifth last code if they exist
        mode1 = codes[numCodes - 3] if numCodes >= 3 else 0
        mode2 = codes[numCodes - 4] if numCodes >= 4 else 0
        mode3 = codes[numCodes - 5] if numCodes >= 5 else 0
        return mode1, mode2, mode3

    def getIndices(self, code):
        program = self.program
        pointer = self.pointer

        index1 = program[pointer + 1]
        # Only setup indices for these if there are appropriate number of params for this code
        index2 = program[pointer + 2] if code == 1 or code == 2 or code == 5 or code == 6 or code == 7 or code == 8 else None
        index3 = program[pointer + 3] if code == 1 or code == 2 or code == 7 or code == 8 else None
        return index1, index2, index3

    # Mode 1 is position mode - read value from position (index)
    # Mode 2 is immediate mode - value is the direct value of the parameter, not value at position
    # Mode 3 is relative mode - read value from position of relative base plus parameter
    def getValue(self, mode, index):
        if mode == 0:
            return self.program[index]
        elif mode == 1:
            return index
        elif mode == 2:
            return self.program[self.relativeBase + index]

    def getWriteAddress(self, mode, index):
        return self.relativeBase + index if mode == 2 else index

    def run(self, inputValue):
        # This loop will stop also if output is reached
        while self.code != 99:
            codes = [int(i) for i in str(self.program[self.pointer])]
            numCodes = len(codes)

            # The code is the two rightmost digits of the instruction, or the last digit for instructions
            # that are lacking modes and are only single digit - handle this with ternary construct
            # Need to combine them to a string to put them together, then re-convert back to int
            code = int(str(codes[numCodes - 2]) + str(codes[numCodes - 1])) if numCodes >= 2 else codes[0]
            self.code = code

            if code == 99:
                break

            mode1, mode2, mode3 = self.getModes(codes, numCodes)
            index1, index2, index3 = self.getIndices(code)
            value1 = self.getValue(mode1, index1)
            # Only get value of second parameter if there is in fact a second parameter present
            value2 = self.getValue(mode2, index2) if index2 != None else None

            if code == 1 or code == 2:
                # Code 1 adds values, code 2 multiplies values
                self.program[self.getWriteAddress(mode3, index3)] = value1 + value2 if code == 1 else value1 * value2
                # Increase pointer by 4, since this instruction uses three parameters
                self.pointer += 4

            elif code == 3:
                if self.testMode == True:
                    try:
                        inputValue = int(input("Input: "))
                    except ValueError:
                        print("Not a number.")
                else:
                    inputValue = self.phase if self.initialInput == True else inputValue

                self.program[self.getWriteAddress(mode1, index1)] = inputValue
                self.initialInput = False
                # Increase pointer by 2, since this instruction has only one parameter
                self.pointer += 2

            elif code == 4:
                # Increase pointer by 2, since this instruction has only one parameter
                self.pointer += 2
                # Output (return) value based on mode
                return value1

            elif code == 5:
                if (value1 != 0):
                    self.pointer = value2
                else:
                    self.pointer += 3
            elif code == 6:
                if (value1 == 0):
                    self.pointer = value2
                else:
                    self.pointer += 3
            elif code == 7:
                self.program[self.getWriteAddress(mode3, index3)] = 1 if value1 < value2 else 0
                self.pointer += 4
            elif code == 8:
                self.program[self.getWriteAddress(mode3, index3)] = 1 if value1 == value2 else 0
                self.pointer += 4
            elif code == 9:
                self.relativeBase += value1
                self.pointer += 2
