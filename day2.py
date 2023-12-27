def star1():
    total = 0
    for line in contents:
        line = line.split(":")
        print(line)
        ids = line[0].split(' ')
        id = ids[-1]
        vals = line[1].split(';')
        maxRed = 12
        maxGreen = 13
        maxBlue = 14
        check = True
        for val in vals:
            totalred = 0
            totalgreen = 0
            val = val.split(',')
            for v in val:
                if "blue" in v:
                    v = v.split(' ')
                    totalblue = int(v[1])
                elif "green" in v:
                    v = v.split(' ')
                    totalgreen = int(v[1])
                else:
                    v = v.split(' ')
                    totalred = int(v[1])
            if (totalblue > maxBlue or totalgreen > maxGreen or totalred > maxRed):
                check = False
        if check:
            total += int(id)

    return total

def star2():
    total = 0
    for line in contents:
        line = line.split(":")
        ids = line[0].split(' ')
        vals = line[1].split(';')
        greens = []
        reds = []
        blues = []
        for val in vals:
            val = val.split(',')
            for v in val:
                if "blue" in v:
                    v = v.split(' ')
                    blues.append(int(v[1]))
                elif "green" in v:
                    v = v.split(' ')
                    greens.append(int(v[1]))
                else:
                    v = v.split(' ')
                    reds.append(int(v[1]))
        total += max(greens) * max(reds) * max(blues)
    return total
lists = []
contents = open("day2.txt").read().splitlines()
print(star1())
print(star2())