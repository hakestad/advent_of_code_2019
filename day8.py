import math
#
#   Part 1
#
file = open("day8_puzzle.txt")
# Read in the file as one big chunk
puzzle = file.read()
# Last char is a newline char, so we remove it
puzzle = puzzle.strip('\n')
# Dimensions of each layer of the image (pixels)
width = 25
height = 6
dim = width * height

numLayers = int(math.ceil(len(puzzle) / dim))
# Initialize a list with the appropriate number of lists (layers) inside
layers = [[] for l in range(0, numLayers)]

for i, char in enumerate(puzzle):
    layerNum = int(math.floor(i/dim))
    layers[layerNum].append(char)

# For the layer with the fewest 0's, we should calculate the number of
# 2's and 1's as well, to multiply their numbers to get the final answer to the puzzle
counter = { "layerIndex": 0, "zeros": 1000000, "ones": 0, "twos": 0 }
for i, layer in enumerate(layers):
    zeros = layer.count('0')
    if zeros < counter["zeros"]:
        counter["layerIndex"] = i
        counter["zeros"] = zeros
        counter["ones"] = layer.count('1')
        counter["twos"] = layer.count('2')

print counter
print "Answer: ", counter["ones"] * counter["twos"]
