def star1():
    total = 0
    string = ''
    for line in contents:
        for val in line:
            if val.isnumeric():
                string += val
                break
        line = line[::-1]
        for val in line:
            if val.isnumeric():
                string += val
                break
        total += int(string)
        string = ''
    return total




def star2():
    total = 0
    list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for line in contents:
        string = ''
        for i, val in enumerate(line):
            if val.isnumeric():
                string += val
            for val in list:
                if line[i:].startswith(val):
                    string += str(list.index(val) + 1)
        total += int(string[0] + string[-1])
    return total


#input
contents = open("day1.txt").read().splitlines()
print(star2())