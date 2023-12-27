from functools import cache
def star1():
    sum = 0
    for line in contents:
        total = 0
        line = line.split(":")[1]
        line = line.split("|")
        vals = line[0].split(" ")
        while "" in vals:
            vals.remove("")
        cards = line[1].split(" ")
        while "" in cards:
            cards.remove("")
        for v in cards:
            if v in vals:
                if total == 0:
                    total = 1
                else:
                    total *= 2
        print(total)
        sum += total
    return sum


copies = dict()
def star2():
    sum = 0
    for line in contents:
        total = 0
        id = line.split(":")[0]
        id = int(id.split(' ')[-1])
        line = line.split(":")[1]
        line = line.split("|")
        vals = line[0].split(" ")
        while "" in vals:
            vals.remove("")
        cards = line[1].split(" ")
        while "" in cards:
            cards.remove("")
        for v in cards:
            if v in vals:
                if total == 0:
                    total = 1
                else:
                    total += 1
        copies[id] = [id + i for i in range(1, total+1)]
    total = 0
    for id in range(1, len(contents) + 1):
        total += (helper(id))
    return total

@cache
def helper(id):
    total = 1
    if len(copies[id]) == 0:
        return 1
    for v in copies[id]:
        total += helper(v)
    return total


contents = open("day4.txt").read().splitlines()
print(star1())
print(star2())