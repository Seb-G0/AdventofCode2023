from collections import defaultdict, deque
from copy import deepcopy

def star1(max_steps):
    grid = [list(row) for row in contents]
    rows = len(grid)
    cols = len(grid[0])
    start_row, start_col = 0, 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start_row, start_col = i, j
                break

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    Os = set()
    distances = defaultdict(lambda: float('inf'))
    distances[(start_row, start_col)] = 0
    Os.add((start_row, start_col))
    for i in range(max_steps):
        new_Os = set()
        for O in Os:
            row, col = O
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] in ['S', '.', 'O']:
                    new_Os.add((new_row, new_col))
        Os = deepcopy(new_Os)

    return len(Os)

def star2():
    grid = [list(row) for row in contents]
    rows = len(grid)
    cols = len(grid[0])
    start_row, start_col = 0, 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start_row, start_col = i, j
                break

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    Os = set()
    distances = defaultdict(lambda: float('inf'))
    distances[(start_row, start_col)] = 0
    Os.add((start_row, start_col))
    for i in range((131 * 2) + 65):
        new_Os = set()
        for O in Os:
            row, col = O
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                shifted_row = new_row % len(grid)
                shifted_col = new_col % len(grid[0])
                if grid[shifted_row][shifted_col] in ['S', '.', 'O']:
                    new_Os.add((new_row, new_col))
        Os = deepcopy(new_Os)
        if ((i + 1) - 65) % 131 == 0:
            print(((i + 1) - 65)//131)
            print(len(Os))

    return len(Os)


contents = open("day21.txt").read().splitlines()
print(star1(64))
print(star2())

x = (26501365 - 65) / 131
a = 14688
b = 14750
c = 3699

print(a * (x * x) + b * x + c)


