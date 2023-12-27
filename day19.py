import re
from copy import deepcopy
def star1():
    workflows = dict()
    values = []
    check = True
    total = 0
    for line in contents:
        if line == '':
            check = False
            continue
        if check:
            name, conditions = line.split("{")
            conditions = conditions[:-1]
            ifs, els = conditions.split(',')[:-1], conditions.split(',')[-1]
            newcons = []
            for val in ifs:
                val = val.split(':')
                for i in val:
                    newcons.append(i)
            workflows[name] = [newcons, els]
            continue
        else:
            pattern = r'\d+'
            numbers = re.findall(pattern, line)
            x, m, a, s = map(int, numbers)
            values.append([x, m, a, s])
    for v in values:
        r = 'in'
        while r != "A" and r != "R":
            workflow = workflows[r]
            e = True
            for c in range(0, len(workflow[0]), 2):
                condition = workflow[0][c]
                if eval(condition):
                    r = workflow[0][c+1]
                    e = False
                    break
            if e:
                r = workflow[1]
        if r == "A":
            total += sum(v)
    return total

def star2():
    workflows = dict()
    check = True
    for line in contents:
        if line == '':
            check = False
            continue
        if check:
            name, conditions = line.split("{")
            conditions = conditions[:-1].split(',')
            workflows[name] = conditions
            continue
    def size(ranges):
        total = 1
        for i in ranges.values():
            total *= i[1] - i[0] + 1
        return total
    def helper(ranges, name):
        total = 0
        for work in workflows[name]:
            if ":" in work:
                condition, result = work.split(":")
                if ">" in condition:
                    var, val = condition.split(">")
                    new_ranges = deepcopy(ranges)
                    if new_ranges[var][1] > int(val):
                        new_ranges[var][0] = max(new_ranges[var][0], int(val) + 1)
                        if result == "A":
                            total += size(new_ranges)
                        elif result != "R":
                            total += helper(new_ranges, result)
                        ranges[var][1] = min(ranges[var][1], int(val))
                if "<" in condition:
                    var, val = condition.split("<")
                    new_ranges = deepcopy(ranges)
                    if new_ranges[var][0] < int(val):
                        new_ranges[var][1] = min(new_ranges[var][1], int(val) - 1)
                        if result == "A":
                            total += size(new_ranges)
                        elif result != "R":
                            total += helper(new_ranges, result)
                        ranges[var][0] = max(ranges[var][0], int(val))
            else:
                if work == "A":
                    total += size(ranges)
                elif work != "R":
                    total += helper(ranges, work)
        return total
    total = helper({"x":[1,4000], "m":[1,4000], "a":[1,4000], "s":[1,4000]}, "in")
    return total

contents = open("day19.txt").read().splitlines()
print(star1())
print(star2())