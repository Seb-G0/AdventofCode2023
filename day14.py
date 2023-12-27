def star1():
    grid = [list(row) for row in contents]
    rocks = []
    hash = []
    for i, row in enumerate(grid):
        for j, r in enumerate(row):
            if r == 'O':
                rocks.append([i, j])
            if r == '#':
                hash.append([i, j])
    for r in rocks:
        while r[0] > 0:
            if [r[0] - 1, r[1]] not in hash and [r[0] - 1, r[1]] not in rocks:
                r[0] -= 1
            else:
                break
    total = 0
    for r in rocks:
        total += len(grid) - r[0]
    return total

mx = 1000000000
def star2():
    grid = [list(row) for row in contents]
    d = {}
    for k in range(mx):

        rows, cols = len(grid), len(grid[0])

        def rotate_to_north(data):
            new_data = [['.'] * cols for _ in range(rows)]
            for j in range(cols):
                to_place = 0
                for i in range(rows):
                    if data[i][j] == '#':
                        new_data[i][j] = '#'
                        to_place = i + 1
                    elif data[i][j] == 'O':
                        new_data[to_place][j] = 'O'
                        to_place += 1
            return new_data

        def rotate_to_west(data):
            new_data = [['.'] * cols for _ in range(rows)]
            for i in range(rows):
                to_place = 0
                for j in range(cols):
                    if data[i][j] == '#':
                        new_data[i][j] = '#'
                        to_place = j + 1
                    elif data[i][j] == 'O':
                        new_data[i][to_place] = 'O'
                        to_place += 1
            return new_data

        def rotate_to_south(data):
            new_data = [['.'] * cols for _ in range(rows)]
            for j in range(cols):
                to_place = rows - 1
                for i in reversed(range(rows)):
                    if data[i][j] == '#':
                        new_data[i][j] = '#'
                        to_place = i - 1
                    elif data[i][j] == 'O':
                        new_data[to_place][j] = 'O'
                        to_place -= 1
            return new_data

        def rotate_to_east(data):
            new_data = [['.'] * cols for _ in range(rows)]
            for i in range(rows):
                to_place = cols - 1
                for j in reversed(range(cols)):
                    if data[i][j] == '#':
                        new_data[i][j] = '#'
                        to_place = j - 1
                    elif data[i][j] == 'O':
                        new_data[i][to_place] = 'O'
                        to_place -= 1
            return new_data
        grid = rotate_to_north(grid)
        grid = rotate_to_west(grid)
        grid = rotate_to_south(grid)
        grid = rotate_to_east(grid)

        tgrid = tuple(tuple(x) for x in grid)
        if tgrid in d:
            diff = k - d[tgrid]
            cycle = (mx - k) % diff - 1
            break
        d[tgrid] = k
    for _ in range(cycle):
        grid = rotate_to_north(grid)
        grid = rotate_to_west(grid)
        grid = rotate_to_south(grid)
        grid = rotate_to_east(grid)
    total = 0
    for g in grid:
        print(''.join(g))
    print(cycle)
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 'O':
                total += len(grid) - i
    return total

contents = open('day14.txt').read().splitlines()
print(star1())
print(star2())




