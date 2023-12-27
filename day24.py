from collections import defaultdict
from sympy import symbols, solve, Eq

def star1():
    minx = miny = 200000000000000
    maxx = maxy = 400000000000000
    equations = []
    for line in contents:
        x, v = line.split(" @ ")
        px, py, pz = str(x).split(', ')
        vx, vy, vz = str(v).split(', ')
        px, py, pz = int(px), int(py), int(pz)
        vx, vy, vz = int(vx), int(vy), int(vz)
        equations.append([px, py, vx, vy])
    count = 0
    for r in range(len(equations)):
        for r2 in range(r + 1, len(equations)):
            px1, py1, vx1, vy1 = equations[r]
            px2, py2, vx2, vy2 = equations[r2]
            slope1 = vy1 / vx1
            slope2 = vy2 / vx2
            eq1 = py1 - slope1 * px1
            eq2 = py2 - slope2 * px2
            if slope1 == slope2:
                continue
            x = (eq2 - eq1) / (slope1 - slope2)
            y = slope1 * x + eq1
            t1 = (x - px1) / vx1
            t2 = (x - px2) / vx2
            if t1 < 0 or t2 < 0:
                continue
            if minx <= x <= maxx and miny <= y <= maxy:
                count += 1
    return count

def star2():
    equations = []
    for line in contents:
        x, v = line.split(" @ ")
        px, py, pz = str(x).split(', ')
        vx, vy, vz = str(v).split(', ')
        px, py, pz = int(px), int(py), int(pz)
        vx, vy, vz = int(vx), int(vy), int(vz)
        equations.append([px, py, pz, vx, vy, vz])
    px, py, pz, pvx, pvy, pvz = symbols('px py pz pvx pvy pvz')
    eq = []
    for i, (x, y, z, vx, vy, vz) in enumerate(equations[:3]):
        t = symbols(f't{i}')
        eq1 = Eq(x + vx * t, px + pvx * t)
        eq2 = Eq(y + vy * t, py + pvy * t)
        eq3 = Eq(z + vz * t, pz + pvz * t)
        for equation in [eq1, eq2, eq3]:
            eq.append(equation)
    solution = solve(eq)
    return solution[0][symbols('px')] + solution[0][symbols('py')] + solution[0][symbols('pz')]

contents = open('day24.txt').read().splitlines()
print(star1())
print(star2())

