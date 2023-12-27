from collections import defaultdict
from math import lcm

def star1():
    data = {}
    low = 0
    high = 0
    for line in contents:
        label, outputs = line.split(' -> ')
        outputs = outputs.split(', ')
        if label == "broadcaster":
            type = -1
            name = label
        else:
            type = label[0]
            name = label[1:]
        data[name] = (type, outputs)
    states = {}
    inputs = defaultdict(list)
    for name in data.keys():
        outputs = data[name][1]
        for o in outputs:
            inputs[o].append(name)
    for name in data.keys():
        type = data[name][0]
        if type == -1:
            continue
        elif type == '%':
            states[name] = False
        elif type == '&':
            state = {}
            for module in inputs[name]:
                state[module] = False
            states[name] = state
    for count in range(1000):
        sent = [('', 'broadcaster', False)]
        while len(sent) > 0:
            newsent = []
            for previous, name, pulse in sent:
                if pulse:
                    high += 1
                else:
                    low += 1
                if data.get(name) == None:
                    continue
                type, outputs = data.get(name)
                if type == '%':
                    if pulse:
                        continue
                    state = states[name]
                    states[name] = not (state)
                    for o in outputs:
                        newsent.append((name, o, not (state)))
                elif type == '&':
                    state = states[name]
                    state[previous] = pulse
                    if sum(state.values()) == len(state):
                        result = False
                    else:
                        result = True
                    for o in outputs:
                        newsent.append((name, o, result))
                elif type == -1:
                    for o in outputs:
                        newsent.append((name, o, pulse))
            sent = newsent[::]
    return low * high


def star2():
    data = {}
    for line in contents:
        label, outputs = line.split(' -> ')
        outputs = outputs.split(', ')
        if label == "broadcaster":
            type = -1
            name = label
        else:
            type = label[0]
            name = label[1:]
        data[name] = (type, outputs)
    states = {}
    inputs = defaultdict(list)
    for name in data.keys():
        outputs = data[name][1]
        for o in outputs:
            inputs[o].append(name)
    for name in data.keys():
        type = data[name][0]
        if type == -1:
            continue
        elif type == '%':
            states[name] = False
        elif type == '&':
            state = {}
            for module in inputs[name]:
                state[module] = False
            states[name] = state
    sources = inputs[inputs['rx'][0]]
    lows = {}
    cycle = 0
    while len(lows) < len(sources):
        cycle += 1
        sent = [('', 'broadcaster', False)]
        while len(sent) > 0:
            newsent = []
            for previous, name, pulse in sent:
                if name in sources:
                    if not(pulse):
                        if name not in lows:
                            lows[name] = cycle
                if data.get(name) == None:
                    continue
                type, outputs = data.get(name)
                if type == '%':
                    if pulse:
                        continue
                    state = states[name]
                    states[name] = not (state)
                    for o in outputs:
                        newsent.append((name, o, not (state)))
                elif type == '&':
                    state = states[name]
                    state[previous] = pulse
                    if sum(state.values()) == len(state):
                        result = False
                    else:
                        result = True
                    for o in outputs:
                        newsent.append((name, o, result))
                elif type == -1:
                    for o in outputs:
                        newsent.append((name, o, pulse))
            sent = newsent[::]
    return lcm(*lows.values())

contents = open("day20.txt").read().splitlines()
print(star1())
print(star2())
