from heapq import heappop, heappush
def inrange(pos, grid):
	return pos[0] in range(len(grid)) and pos[1] in range(len(grid[0]))

def star1(mn, mx):
	grid = [list(map(int, row)) for row in contents]
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	seen = set()
	costs = {}
	q = [(0, 0, 0, -1)]
	while q:
		cost, x, y, d = heappop(q)
		if x == len(grid) - 1 and y == len(grid[0]) - 1:
			return cost
		if (x, y, d) in seen:
			continue
		seen.add((x, y, d))
		for direction in range(4):
			costinc = 0
			if direction == d or (direction + 2) % 4 == d:
				continue
			for distance in range(1, mx + 1):
				newx = x + directions[direction][0] * distance
				newY = y + directions[direction][1] * distance
				if inrange((newx, newY), grid):
					costinc += grid[newx][newY]
					if distance < mn:
						continue
					newCost = cost + costinc
					if costs.get((newx, newY, direction), 10000000) <= newCost:
						continue
					costs[(newx, newY, direction)] = newCost
					heappush(q, (newCost, newx, newY, direction))




def star2():
	return star1(4, 10)

contents = open("day17.txt").read().splitlines()
print(star1(1, 3))
print(star2())
