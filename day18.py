import numpy as np

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

def star1():
    edges = set()
    location = (0, 0)
    xs = []
    ys = []
    directions = {
        "R" : [0, 1],
        "L" : [0, -1],
        "U" : [-1, 0],
        "D" : [1, 0],}
    for line in contents:
        dir, dist, color = line.split(' ')
        x, y = directions[dir]
        dist = int(dist)
        for r in range(1, dist + 1):
            edges.add((location[0] + (x * r), location[1] + (y * r)))
        location = (location[0] + (x * dist),  location[1] + (y * dist))
        xs.append(location[0])
        ys.append(location[1])
    A = PolyArea(xs, ys)
    b = len(edges)
    I = A + 1 - b // 2
    return I + b

def star2():
    location = (0, 0)
    xs = []
    ys = []
    num = 0
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    for line in contents:
        dir, dist, color = line.split(' ')
        x, y = directions[int(color[-2])]
        dist = int(color[-7: - 2], 16)
        num += dist
        location = (location[0] + (x * dist),  location[1] + (y * dist))
        xs.append(location[0])
        ys.append(location[1])
    A = PolyArea(xs, ys)
    b = num
    I = A + 1 - b // 2
    return I + b

contents = open('day18.txt').read().splitlines()
print(star1())
print(star2())