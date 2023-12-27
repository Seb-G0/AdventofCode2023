def star1():
    lasts = []
    for nums in [list(map(int, line.strip().split())) for line in contents]:
        history = [[nums[i] for i in range(len(nums))]]
        values = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        history.append(values)
        while set(values) != {0}:
            values = [values[i] - values[i - 1] for i in range(1, len(values))]
            history.append(values)
        history.reverse()
        history[0].append(0)
        for i in range(1, len(history)):
            history[i].insert(len(history[i]), history[i][-1] + (1) * history[i - 1][-1])
        lasts.append(history[-1][-1])
    return sum(lasts)

def star2():
    lasts = []
    for nums in [list(map(int, line.strip().split())) for line in contents]:
        history = [[nums[i] for i in range(len(nums))]]
        values = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        history.append(values)
        while set(values) != {0}:
            values = [values[i] - values[i - 1] for i in range(1, len(values))]
            history.append(values)
        history.reverse()
        history[0].append(0)
        for i in range(1, len(history)):
            history[i].insert(0, history[i][0] + (-1) * history[i - 1][0])
        lasts.append(history[-1][0])
    return sum(lasts)

contents = open("day9.txt").read().splitlines()
print(star1())
print(star2())