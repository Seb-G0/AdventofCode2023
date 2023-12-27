def star1():
    seeds = list(map(int, contents[0].split(" ")[1:]))
    converter = dict()

    def retrieve(name, value):
        for range in converter[name]:
            next = range[0]
            source = range[1]
            count = range[2]
            if value >= source and value < source + count:
                return value + (next - source)
        return value

    start = True
    for line in contents[2:]:
        if line == '':
            start = True
            continue
        elif start:
            name = line.split('-')[0]
            converter[name] = []
            start = False
        else:
            line = line.split(" ")
            next = int(line[0])
            incr = int(line[2])
            source = int(line[1])
            converter[name].append([next, source, incr])

    vals = []
    for value in seeds:
        for name in converter:
            value = retrieve(name, value)
        vals.append(value)
    return (min(vals))

def star2():
    seeds = list(map(int, contents[0].split(" ")[1:]))
    seeds = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds) - 1, 2)]
    converter = dict()
    start = True
    for line in contents[2:]:
        if line == '':
            start = True
            continue
        elif start:
            name = line.split('-')[0]
            converter[name] = []
            start = False
        else:
            line = line.split(" ")
            next = int(line[0])
            incr = int(line[2])
            source = int(line[1])
            converter[name].append([next, source, incr])


    def overlap(r1, r2):
        a, b = r1
        c, d = r2
        return max(a, c) < min(b, d)

    def transform(rng, shift):
        return (rng[0] + shift, rng[1] + shift)

    values = []
    for r in seeds:
        ranges = [r]
        for name in converter.keys():
            newRanges = []
            current = converter[name]
            for rng in ranges:
                for c in current:
                    compareTo = (c[1], c[1] + c[2] - 1)
                    next = c[0]
                    source = c[1]
                    if overlap(rng, compareTo):
                        overlap_range = (max(rng[0], compareTo[0]), min(rng[1], compareTo[1]))
                        newRanges.append(transform(overlap_range, next - source))
            if len(newRanges) != 0:
                ranges = newRanges
        values.append(min(ranges)[0])
    return min(values)


contents = open("day5.txt").read().splitlines()
print(star1())
print(star2())