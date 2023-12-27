from collections import deque, defaultdict
def star1():
    grid = [list(row) for row in contents]

    neighbors = defaultdict(list)
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            n = []
            if cell == "|":
                n = [(i - 1, j), (i + 1, j)]
            elif cell == "-":
                n = [(i, j - 1), (i, j + 1)]
            elif cell == "L":
                n = [(i - 1, j), (i, j + 1)]
            elif cell == "J":
                n = [(i - 1, j), (i, j - 1)]
            elif cell == "7":
                n = [(i + 1, j), (i, j - 1)]
            elif cell == "F":
                n = [(i + 1, j), (i, j + 1)]
            elif cell == "S":
                start = (i, j)
            for x, y in n:
                if x >= 0 and x < len(grid) and y >= 0 and y < len(row):
                    neighbors[(i, j)].append((x, y))
    connected = []
    for point in neighbors:
        if start in neighbors[point]:
            connected.append(point)
    neighbors[start] = connected
    queue = [(start, 0)]
    visited = set([start])
    max_distance = 0
    while queue:
        curr_pos, distance = queue.pop(0)
        max_distance = max(max_distance, distance)
        for direction in neighbors[curr_pos]:
            if direction not in visited:
                queue.append((direction, distance + 1))
                visited.add(direction)
    return max_distance

def star2():
    grid = [list(row) for row in contents]
    start_pos = False
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                start_pos = (x, y)
                break
        if start_pos:
            break
    neighbors = defaultdict(list)
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            n = []
            if cell == "|":
                n = [(2 * i - 1, 2 * j), (2 * i + 1, 2 * j)]
            elif cell == "-":
                n = [(2 * i, 2 * j - 1), (2 * i, 2 * j + 1)]
            elif cell == "L":
                n = [(2 * i - 1, 2 * j), (2 * i, 2 * j + 1)]
            elif cell == "J":
                n = [(2 * i - 1, 2 * j), (2 * i, 2 * j - 1)]
            elif cell == "7":
                n = [(2 * i + 1, 2 * j), (2 * i, 2 * j - 1)]
            elif cell == "F":
                n = [(2 * i + 1, 2 * j), (2 * i, 2 * j + 1)]
            elif cell == "S":
                start = (2 * i, 2 * j)
            for x, y in n:
                if x >= 0 and x < 2 * len(grid) and y >= 0 and y < 2 * len(row):
                    neighbors[(2 * i, 2 * j)].append((x, y))

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            xs = []
            if i > 0:
                xs.append(2 * i - 1)
            if i + 1 < len(grid):
                xs.append(2 * i + 1)
            ys = []
            if j > 0:
                ys.append(2 * j - 1)
            if j + 1 < len(row):
                ys.append(2 * j + 1)
            for nx in xs:
                neighbors[(nx, 2 * j)].append((2 * i, 2 * j))
            for ny in ys:
                neighbors[(2 * i, ny)].append((2 * i, 2 * j))
    starts = []
    near = defaultdict(int)
    for n in neighbors:
        for val in neighbors[n]:
            near[val] += 1
            if val == start:
                starts.append(n)
    for n in starts:
        if near[n] > 0:
            neighbors[start].append(n)
    distance = defaultdict(lambda: float('inf'))
    queue = deque()
    queue.append(start)
    distance[start] = 0
    inloop = set()
    while len(queue) > 0:
        curr = queue.popleft()
        inloop.add(curr)
        for n in neighbors[curr]:
            if distance[n] == float('inf'):
                distance[n] = distance[curr] + 1
                queue.append(n)
    total = 0
    vis = set()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (2 * i, 2 * j) in inloop or (2 * i, 2 * j) in vis:
                continue
            visited = set()
            queue = deque()
            queue.append((2 * i, 2 * j))
            visited.add((2 * i, 2 * j))
            enclosed = True
            while len(queue) > 0:
                x, y = queue.popleft()
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if (nx, ny) in inloop or (nx, ny) in visited:
                        continue
                    if nx < 0 or nx >= 2 * len(grid) or ny < 0 or ny >= 2 * len(row):
                        enclosed = False
                        continue
                    queue.append((nx, ny))
                    visited.add((nx, ny))
            for val in visited:
                if val[0] % 2 == 0 and val[1] % 2 == 0 and enclosed:
                    total += 1
                vis.add(val)
    return total


contents = open('day10.txt').read().splitlines()
print(star1())
print(star2())