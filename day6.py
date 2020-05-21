
def countOrbits(key, dict, count):
    val = dict[key]
    if dict.get(val) == None:
        return(count)
    else:
        return(countOrbits(val, dict, count + 1))

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

numOrbits = 0
for key in orbits:
    numOrbits += countOrbits(key, orbits, 1)

print "Number of direct and indirect orbits: ", numOrbits
