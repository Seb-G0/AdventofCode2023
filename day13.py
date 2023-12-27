from collections import defaultdict
from collections import Counter


def star1():
    total = 0
    grids = []
    grid = []
    for line in contents:
        if line == '':
            grids.append(grid)
            grid = []
        else:
            grid.append(line)
    for grid in grids:
        rows = [list(row) for row in grid]
        cols = [column for column in zip(*grid)]
        for r in range(len(rows) - 1):
            if rows[r] == rows[r + 1]:
                i = 1
                t = r
                check = True
                while r + i < len(rows) and t >= 0:
                    if rows[t] != rows[r + i]:
                        check = False
                        break
                    i += 1
                    t -= 1
                if check:
                    total += 100 * (r + 1)
        for c in range(len(cols) - 1):
            if cols[c] == cols[c + 1]:
                i = 1
                t = c
                check = True
                while c + i < len(cols) and t >= 0:
                    if cols[t] != cols[c + i]:
                        check = False
                        break
                    i += 1
                    t -= 1
                if check:
                    total += (c + 1)
    return total

def star2():
    total = 0
    grids = []
    grid = []
    for line in contents:
        if line == '':
            grids.append(grid)
            grid = []
        else:
            grid.append(line)
    for grid in grids:
        rows = [list(row) for row in grid]
        cols = [column for column in zip(*grid)]
        for r in range(len(rows) - 1):
            i = 1
            t = r
            smudges = 0
            while r + i < len(rows) and t >= 0:
                r1 = rows[t]
                r2 = rows[r + i]
                for v1, v2 in zip(r1, r2):
                    if v1 != v2:
                        smudges += 1
                i += 1
                t -= 1
            if smudges == 1:
                total += (r + 1) * 100
        for c in range(len(cols) - 1):
            smudges = 0
            i = 1
            t = c
            while c + i < len(cols) and t >= 0:
                c1 = cols[t]
                c2 = cols[c + i]
                for v1, v2 in zip(c1, c2):
                    if v1 != v2:
                        smudges += 1
                i += 1
                t -= 1
            if smudges == 1:
                total += (c + 1)
    return total

contents = open('day13.txt').read().splitlines()
print(star1())
print(star2())
