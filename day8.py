import math
from PIL import Image
import numpy as np
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

print ("Answer, part 1: ", counter["ones"] * counter["twos"])

#
#   Part 2
#
pixels = [[], [], [], [], [], []]
for l, layer in enumerate(layers):
    for h in range(0, height):
        for w in range (0, width):
            # Layer is not split into row and column, it's just one line
            candidatePixel = layer[((h+1)*width) - (width - w)]
            # If this is the first layer we're inspecting
            if l == 0:
                pixels[h].append(candidatePixel)
            else:
                currentPixel = pixels[h][w]
                # If currentPixel is transparent, we'll use the pixel in the
                # layer underneath instead
                if currentPixel == '2':
                    pixels[h][w] = candidatePixel

#
# For fun, turn it into an actual image
#
# First setting up color codes for the pixels
colorPixels = [[], [], [], [], [], []]
for i, row in enumerate(pixels):
    for j, pixel in enumerate(row):
        colorPixel = (0,0,0) if pixel == '0' else (255,255,255)
        colorPixels[i].append(colorPixel)


# Convert the pixels into an array using numpy
array = np.array(colorPixels, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels
image = Image.fromarray(array)
image.save('day8_part2.png')

#
#   But also output to terminal
#
for row in pixels:
    row = [" " if x == '0' else "#" for x in row]
    print(" ".join(row))
