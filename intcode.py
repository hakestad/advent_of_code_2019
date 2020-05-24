#
#   Starting afresh, because the code from day 2 and 5 was kinda bad
#   Going for a better structure here, using an object oriented approach
#   for easier control of each Intcode object's state
#

class Intcode:
    def __init__(self, program, phase, pointer):
        self.phase = phase
        self.pointer = pointer
        self.program = program
        self.code = 0
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

    def run(self, inputValue):

        while self.code != 99:
            codes = [int(i) for i in str(self.program[self.pointer])]
            numCodes = len(codes)

            # The code is the two rightmost digits of the instruction, or the last digit for instructions
            # that are lacking modes and are only single digit - handle this with ternary construct
            # Need to combine them to a string to put them together, then re-convert back to int
            code = int(`codes[numCodes - 2]` + `codes[numCodes - 1]`) if numCodes >= 2 else codes[0]
            self.code = code

            if code == 99:
                break

            mode1, mode2, mode3 = self.getModes(codes, numCodes)
            index1, index2, index3 = self.getIndices(code)

            if code == 1:
                # Depending on the mode, you should either add the values at
                # the indexed positions (mode == 0) together, or add the
                # direct values (indices) together (mode == 1)
                a1 = self.program[index1] if mode1 == 0 else index1
                a2 = self.program[index2] if mode2 == 0 else index2

                self.program[index3] = a1 + a2
                # Increase pointer by 4, since this instruction uses three parameters
                self.pointer += 4
            elif code == 2:
                # For code 2, you should multiply instead
                m1 = self.program[index1] if mode1 == 0 else index1
                m2 = self.program[index2] if mode2 == 0 else index2
                self.program[index3] = m1 * m2
                # Increase pointer by 4, since this instruction uses three parameters
                self.pointer += 4

            elif code == 3:
                self.program[index1] = self.phase if self.initialInput == True else inputValue
                self.initialInput = False
                # Increase pointer by 2, since this instruction has only one parameter
                self.pointer += 2

            elif code == 4:
                # Output value at the position given by the first parameter, or the index value if mode == 1
                output = self.program[index1] if mode1 == 0 else index1
                # Increase pointer by 2, since this instruction has only one parameter
                self.pointer += 2
                return output

            elif code == 5:
                firstParam = self.program[index1] if mode1 == 0 else index1
                if (firstParam != 0):
                    self.pointer = self.program[index2] if mode2 == 0 else index2
                else:
                    self.pointer += 3
            elif code == 6:
                firstParam = self.program[index1] if mode1 == 0 else index1
                if (firstParam == 0):
                    self.pointer = self.program[index2] if mode2 == 0 else index2
                else:
                    self.pointer += 3
            elif code == 7:
                firstParam = self.program[index1] if mode1 == 0 else index1
                secondParam = self.program[index2] if mode2 == 0 else index2
                self.program[index3] = 1 if firstParam < secondParam else 0
                self.pointer += 4
            elif code == 8:
                firstParam = self.program[index1] if mode1 == 0 else index1
                secondParam = self.program[index2] if mode2 == 0 else index2
                self.program[index3] = 1 if firstParam == secondParam else 0
                self.pointer += 4
