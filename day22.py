from collections import defaultdict
contents = open('day22.txt').read().splitlines()
def drop(tower):
    tallest = defaultdict(int)
    new_tower = []
    falls = 0
    for brick in tower:
        deltaZ = max(brick[2] - max(tallest[(x, y)] for x in range(brick[0], brick[3] + 1) for y in range(brick[1], brick[4] + 1)) - 1, 0)
        new_brick = (brick[0], brick[1], brick[2] - deltaZ, brick[3], brick[4], brick[5] - deltaZ)
        if new_brick[2] != brick[2]:
            falls += 1
        new_tower.append(new_brick)
        for x in range(brick[0], brick[3] + 1):
            for y in range(brick[1], brick[4] + 1):
                tallest[(x, y)] = new_brick[5]
    return falls, new_tower

def star1():
    count = 0
    bricks = []
    for line in contents:
        positions = line.split('~')
        start = tuple(map(int, positions[0].split(',')))
        end = tuple(map(int, positions[1].split(',')))
        bricks.append(start + end)
    bricks = sorted(bricks, key=lambda x: x[2])
    falls, tower = drop(bricks)
    for i in range(len(tower)):
        removed = tower[:i] + tower[i + 1:]
        falls, t = drop(removed)
        if falls != 0:
            count += 1
    return count

def star2():
    count = 0
    bricks = []
    for line in contents:
        positions = line.split('~')
        start = tuple(map(int, positions[0].split(',')))
        end = tuple(map(int, positions[1].split(',')))
        bricks.append(start + end)
    bricks = sorted(bricks, key=lambda x: x[2])
    falls, tower = drop(bricks)
    for i in range(len(tower)):
        removed = tower[:i] + tower[i + 1:]
        falls, t = drop(removed)
        count += falls
    return count


print(star1())
print(star2())

