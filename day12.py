from collections import defaultdict
from functools import lru_cache

def star1():
    total = 0
    for line in contents:
        line, plan = line.split(' ')
        plan = list(map(int, plan.split(",")))
        @lru_cache(maxsize = None)
        def builder(posLine, planCord, currentLength):
            sum = 0
            if posLine == len(line):
                if currentLength == 0 and planCord == len(plan):
                    return 1
                elif planCord < len(plan):
                    if currentLength == plan[planCord] and len(plan) - 1 == planCord:
                        return 1
                return 0
            for possible in ['.', '#']:
                if line[posLine] == '?' or possible == line[posLine]:
                    if possible == '.' and currentLength == 0:
                        sum += builder(posLine + 1, planCord, currentLength)
                    elif possible == '.' and currentLength != 0 and planCord < len(plan) and plan[planCord] == currentLength:
                        sum += builder(posLine + 1, planCord + 1, 0)
                    elif possible == '#':
                        sum += builder(posLine + 1, planCord, currentLength + 1)
            return sum
        total += builder(0, 0, 0)
    return total



def star2():
    total = 0
    for line in contents:
        line, plan = line.split(' ')
        line = '?'.join([line, line, line, line, line])
        plan = ','.join([plan, plan, plan, plan, plan])
        plan = list(map(int, plan.split(',')))
        @lru_cache(maxsize= None)
        def builder(posLine, planCord, currentLength):
            sum = 0
            if posLine == len(line):
                if currentLength == 0 and planCord == len(plan):
                    return 1
                elif planCord < len(plan):
                    if currentLength == plan[planCord] and len(plan) - 1 == planCord:
                        return 1
                return 0
            for possible in ['.', '#']:
                if line[posLine] == '?' or possible == line[posLine]:
                    if possible == '.' and currentLength == 0:
                        sum += builder(posLine + 1, planCord, currentLength)
                    elif possible == '.' and currentLength != 0 and planCord < len(plan) and plan[planCord] == currentLength:
                        sum += builder(posLine + 1, planCord + 1, 0)
                    elif possible == '#':
                        sum += builder(posLine + 1, planCord, currentLength + 1)
            return sum
        total += builder(0, 0, 0)
    return total

contents = open("day12.txt").read().splitlines()
print(star1())
print(star2())