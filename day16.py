from collections import defaultdict
from time import time
def star1():
    beams = [(0, -1, "E")]
    directions = {
                "S" : [1, 0],
                "N" : [-1, 0],
                "E" : [0, 1],
                "W" : [0, -1]
            }
    energized = set()
    allBeams = set()
    while len(beams) > 0:
        b = beams.pop(0)
        if b in allBeams:
            continue
        energized.add((b[0], b[1]))
        allBeams.add(b[::])
        direction = directions[b[2]]
        x, y, d = b[0], b[1], b[2]
        x += direction[0]
        y += direction[1]
        if min(x, y) < 0 or x >= len(contents) or y >= len(contents[0]):
            continue
        else:
            val = contents[x][y]
            if val == '\\':
                if d == "N":
                    d = "W"
                elif d == "W":
                    d = "N"
                elif d == "S":
                    d = "E"
                elif d == "E":
                    d = "S"
            elif val == '/':
                if d == "S":
                    d = "W"
                elif d == "W":
                    d = "S"
                elif d == "N":
                    d = "E"
                elif d == "E":
                    d = "N"
            elif val == '-':
                if d == "E" or d == "W":
                    pass
                else:
                    d = "E"
                    beams.append((x, y, "W"))
            elif val == '|':
                if d == "N" or d == "S":
                    pass
                else:
                    d = "N"
                    beams.append((x, y, "S"))
            beams.append((x, y, d))
    return len(energized) - 1

def star2():
    beamers = [(row, -1, "E") for row in range(len(contents[0]))] + [(row, len(contents[0]), "W") for row in range(
    len(contents[0]))] + [(-1, col, "S") for col in range(len(contents))] + [(len(contents), col, "N") for col in range(len(contents))]
    energies = set()
    for beams in beamers:
        beams = [beams]
        directions = {
            "S": [1, 0],
            "N": [-1, 0],
            "E": [0, 1],
            "W": [0, -1]
        }
        energized = set()
        allBeams = set()
        while len(beams) > 0:
            b = beams.pop(0)
            if b in allBeams:
                continue
            energized.add((b[0], b[1]))
            allBeams.add(b[::])
            direction = directions[b[2]]
            x, y, d = b[0], b[1], b[2]
            x += direction[0]
            y += direction[1]
            if min(x, y) < 0 or x >= len(contents) or y >= len(contents[0]):
                continue
            else:
                val = contents[x][y]
                if val == '\\':
                    if d == "N":
                        d = "W"
                    elif d == "W":
                        d = "N"
                    elif d == "S":
                        d = "E"
                    elif d == "E":
                        d = "S"
                elif val == '/':
                    if d == "S":
                        d = "W"
                    elif d == "W":
                        d = "S"
                    elif d == "N":
                        d = "E"
                    elif d == "E":
                        d = "N"
                elif val == '-':
                    if d == "E" or d == "W":
                        pass
                    else:
                        d = "E"
                        beams.append((x, y, "W"))
                elif val == '|':
                    if d == "N" or d == "S":
                        pass
                    else:
                        d = "N"
                        beams.append((x, y, "S"))
                beams.append((x, y, d))
        energies.add(len(energized) - 1)
    return max(energies)


contents = open("day16.txt").read().splitlines()
print((star1()))
print((star2()))
