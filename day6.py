def star1():
    total = 1
    times = [t for t in contents[0].split(":")[1].strip().split(" ")]
    while "" in times:
        times.remove("")
    distances = [d for d in contents[1].split(":")[1].strip().split(" ")]
    while "" in distances:
        distances.remove("")
    for v in range(len(times)):
        count = 0
        time = int(times[v])
        distance = int(distances[v])
        print(time, distance)
        for t in range(time):
            speed = t
            timeleft = time - t
            distancecovered = speed * timeleft
            if distancecovered > distance:
                count += 1
        total *= count
    return total


def star2():
    times = [t for t in contents[0].split(":")[1].strip().split(" ")]
    while "" in times:
        times.remove("")
    distances = [d for d in contents[1].split(":")[1].strip().split(" ")]
    while "" in distances:
        distances.remove("")
    time = ''
    distance = ''
    for t in times:
        time += t
    for d in distances:
        distance += d
    time = int(time)
    distance = int(distance)
    print((int((time + (time * time - 4*distance) ** 0.5)/2) + 1) - (int((time - (time * time - 4*distance) ** 0.5)/2) + 1))


contents = open("day6.txt").read().splitlines()
print(star1())
print(star2())
