from collections import defaultdict
import sys
from time import time
sys.setrecursionlimit(10000)
def star1():
    grid = [list(row) for row in contents]
    rows, cols = len(grid), len(grid[0])
    for i in range(len(contents[0])):
        if contents[0][i] == '.':
            sx, sy, dist = 0, i, 0
    for i in range(len(contents[-1])):
        if contents[-1][i] == '.':
            goal = i
    goal = (len(contents) - 1, goal)
    distance = [[0 for _ in range(cols)] for _ in range(rows)]
    slopes = {'v' : [1, 0], '>' : [0, 1], '<' : [0, -1]}

    def is_valid_move(x, y, path):
        rows, cols = len(grid), len(grid[0])
        return 0 <= x < rows and 0 <= y < cols and not (x, y) in path and grid[x][y] != '#'

    def get_neighbors(x, y, path):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbors = []
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y, path):
                neighbors.append((new_x, new_y))
        return neighbors

    def dfs(x, y, path):
        if (x, y) in path:
            return
        if (x, y) == goal:
            distance[x][y] = max(distance[x][y], len(path))
        path = path + [(x, y)]
        for nx, ny in get_neighbors(x, y, path):
            if grid[nx][ny] in slopes:
                slope = slopes[grid[nx][ny]]
                if [(nx - x), (ny - y)] != slope:
                    continue
                dfs(nx + slope[0], ny + slope[1], path + [(nx, ny)])
            else:
                dfs(nx, ny, path)

    dfs(sx, sy, [])
    return distance[goal[0]][goal[1]]

def star2():
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    adjacency = defaultdict(lambda: set())
    for x, row in enumerate(contents):
        for y, v in enumerate(row):
            if v != '#':
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < len(contents) and 0 <= ny < len(row)) and contents[nx][ny] != '#':
                        adjacency[(x, y)].add((nx, ny, 1))
                        adjacency[(nx, ny)].add((x, y, 1))
    while True:
        for key, neighbors in adjacency.items():
            if len(neighbors) == 2:
                n1, n2 = neighbors
                pos1 = n1[:-1]
                pos2 = n2[:-1]
                length1 = n1[-1]
                length2 = n2[-1]
                name1 = key + (length1,)
                name2 = key + (length2,)
                adjacency[pos1].remove(name1)
                adjacency[pos2].remove(name2)
                adjacency[pos1].add((pos2[0], pos2[1], length1 + length2))
                adjacency[pos2].add((pos1[0], pos1[1], length1 + length2))
                del adjacency[key]
                break
        else:
            break
    grid = [list(row) for row in contents]
    rows, cols = len(grid), len(grid[0])
    for i in range(len(contents[0])):
        if contents[0][i] == '.':
            sx, sy, dist = 0, i, 0
    for i in range(len(contents[-1])):
        if contents[-1][i] == '.':
            goal = i
    goal = (len(contents) - 1, goal)
    distance = [[0 for _ in range(cols)] for _ in range(rows)]

    def dfs(x, y, path, length):
        if (x, y) in path:
            return
        if (x, y) == goal:
            distance[x][y] = max(distance[x][y], length)
        path = path + [(x, y)]
        for nx, ny, l in adjacency[(x, y)]:
            dfs(nx, ny, path, length + l)
    dfs(sx, sy, [], 0)

    return distance[goal[0]][goal[1]]
contents = open("day23.txt").read().splitlines()
start1 = time()
print(star1())
print(time() - start1)
start2 = time()
print(star2())
print(time() - start2)
