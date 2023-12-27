def star1():
  num = 1
  stars = [[i, j] for i, row in enumerate(contents) for j, column in enumerate(row) if column == '#']
  for i in range(len(contents) - 1, -1, -1):
    row = contents[i]
    if all(col == '.' for col in row):
      for star in stars:
        if star[0] > i:
          star[0] += num

  for j in range(len(contents) - 1, -1, -1):
    if all(row[j] == '.' for row in contents):
      for star in stars:
        if star[1] > j:
          star[1] += num

  return sum([abs(stars[star1][0] - stars[star2][0]) + abs(stars[star1][1] - stars[star2][1]) for star1 in range(len(stars)) for star2 in range(star1 + 1, len(stars))])

def star2():
  num = 999999
  stars = [[i, j] for i, row in enumerate(contents) for j, column in enumerate(row) if column == '#']
  for i in range(len(contents) - 1, -1, -1):
    row = contents[i]
    if all(col == '.' for col in row):
      for star in stars:
        if star[0] > i:
          star[0] += num

  for j in range(len(contents) - 1, -1, -1):
    if all(row[j] == '.' for row in contents):
      for star in stars:
        if star[1] > j:
          star[1] += num

  return sum([abs(stars[star1][0] - stars[star2][0]) + abs(stars[star1][1] - stars[star2][1]) for star1 in range(len(stars)) for star2 in range(star1 + 1, len(stars))])

contents = open("day11.txt").read().splitlines()
print(star1())
print(star2())
