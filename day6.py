#
#   Part 1
#

# Recursive function to count the number of direct and indirect orbits
def countOrbits(key, dict, count):
    val = dict[key]
    if dict.get(val) == None:
        return(count)
    else:
        return(countOrbits(val, dict, count + 1))

# Use a dictionary to keep track of which is orbiting which
orbits = {}
with open("day6_puzzle.txt") as puzzle:
    # Each line represent a relationship, where one is the orbitee and
    # the other is orbiting the former
    for line in puzzle:
        # Use list comprehension to both split and strip line of whitespace at the same time
        line = [part.strip() for part in line.split(')')]
        # The one being orbited is the one on the left of the )
        orbitee = line[0]
        # while the one that orbits is the one on the right of the )
        orbiter = line[1]
        #print 'orbitee: ', orbitee
        #print 'orbiter: ', orbiter
        orbits[orbiter] = orbitee

# add up the number that each item in the dictionary is orbiting another object
# either directly or indirectly
numOrbits = 0
for key in orbits:
    numOrbits += countOrbits(key, orbits, 1)

print "Number of direct and indirect orbits: ", numOrbits

#
#   Part 2
#

# Create a list of the direct and indirect orbits from a starting position (key)
def makeOrbitalTraversionMap(key, dict, map):
    val = dict[key]
    if (dict.get(val) == None):
        return(map)
    else:
        map.append(val)
        return(makeOrbitalTraversionMap(val, dict, map))

# Find number of orbits between one position and another
def countOrbitsFromTo(fromPos, toPos, dict, count):
    val = dict[fromPos]
    if dict.get(val) == toPos:
        return(count)
    else:
        return(countOrbitsFromTo(val, toPos, dict, count + 1))

# Map all the objects Santa orbits, as a path from outer to inner
map1 = makeOrbitalTraversionMap("SAN", orbits, [])
# and the same for yourself
map2 = makeOrbitalTraversionMap("YOU", orbits, [])

# Find where the two paths intersects, so that we know the position from
# which to backtrack and count so that we can figure out how many orbital
# transfers are needed to take for YOU to orbit around the same object as SAN
intersections = [x for x in map1 if x in map2]
firstIntersect = intersections[0]

count1 = countOrbitsFromTo("SAN", firstIntersect, orbits, 1)
count2 = countOrbitsFromTo("YOU", firstIntersect, orbits, 1)

print "Number of orbital transfers: ", count1 + count2
