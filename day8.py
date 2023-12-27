from collections import defaultdict
from math import lcm
def star1():
    inp = contents[0]
    steps = 0
    values = defaultdict(list)
    for line in contents[2:]:
        line = line.split(" = ")
        lst = line[1][1:-1].split(', ')
        values[line[0]] = lst
    place = ["AAA"]
    while not(all('Z' in str(x) for x in place)):
        for i in inp:
            if i == "R":
                move = 1
            else:
                move = 0
            for i, p in enumerate(place):
                place[i] = values[p][move]
            steps += 1
            if all('Z' in str(x) for x in place):
                break
    return steps

def star2():
    inp = contents[0]
    place = []
    values = defaultdict(list)
    for line in contents[2:]:
        line = line.split(" = ")
        lst = line[1][1:-1].split(', ')
        if "A" in line[0]:
            place.append(line[0])
        values[line[0]] = lst
    lcms = []
    for p in place:
        steps = 0
        while "Z" not in p:
            for i in inp:
                if i == "R":
                    move = 1
                else:
                    move = 0
                p = values[p][move]
                steps += 1
            if "Z" in p:
                break
        lcms.append(steps)
    return lcm(*lcms)

contents = open("day8.txt").read().splitlines()
print(star1())
print(star2())