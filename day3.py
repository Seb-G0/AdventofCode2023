def star1():
    total = 0
    for i in range(len(contents)):
        for j in range(len(contents[i])):
            if not(contents[i][j].isalnum()) and contents[i][j] != '.':
                seen = []
                for k in range(i-1, i+2):
                    for l in range(j - 1, j +2):
                        string = contents[k][l]
                        if contents[k][l].isnumeric():
                            for m in range(l-1, -1, -1):
                                if contents[k][m].isnumeric():
                                    string = contents[k][m] + string
                                else:
                                    break
                            for m in range(l+1, len(contents[0])):
                                if contents[k][m].isnumeric():
                                    string += contents[k][m]
                                else:
                                    break
                            if not(string in seen):
                                print(string)
                                seen.append(string)

                                total += int(string)


    return total



def star2():
    total = 0
    for i in range(len(contents)):
        for j in range(len(contents[i])):
            if contents[i][j] == '*':
                seen = []
                for k in range(i-1, i+2):
                    for l in range(j - 1, j +2):
                        string = contents[k][l]
                        if contents[k][l].isnumeric():
                            for m in range(l-1, -1, -1):
                                if contents[k][m].isnumeric():
                                    string = contents[k][m] + string
                                else:
                                    break
                            for m in range(l+1, len(contents[0])):
                                if contents[k][m].isnumeric():
                                    string += contents[k][m]
                                else:
                                    break
                            if not(string in seen):
                                seen.append(string)
                if len(seen) == 2:
                    total += int(seen[0]) * int(seen[1])


    return total




contents = open("day3.txt").read().splitlines()
print(star1())
print(star2())

