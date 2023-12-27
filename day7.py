from collections import defaultdict

def star1():
    hands = defaultdict(list)
    bids = {}
    for line in contents:
        d = defaultdict(int)
        hand, bid = line.split(" ")
        bid = int(bid)
        bids[hand] = bid
        for c in hand:
            d[c] += 1
        if max(d.values()) == 5:
            rank = 5
        elif max(d.values()) == 4:
            rank = 4
        elif max(d.values()) == 3 and min(d.values()) == 2:
            rank = 3
        elif max(d.values()) == 3:
            rank = 2
        elif list(d.values()).count(2) == 2:
            rank = 1
        elif list(d.values()).count(2) == 1 :
            rank = 0
        else:
            rank = -1
        hands[rank].append(hand)
    placements = []
    cardrankings = {"K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "A": 14}
    for key in range(-1, 6):
        grouping = hands[key]
        grouping.sort(key=lambda x: [cardrankings[char] for char in x], reverse=True)
        grouping.reverse()
        for i in grouping:
            placements.append(i)
    total = 0
    for i, h in enumerate(placements):
        total += (i+1) * bids[h]
    return total

def star2():
    hands = defaultdict(list)
    bids = {}
    for line in contents:
        hand, bid = line.split(" ")
        bid = int(bid)
        bids[hand] = bid
        rank = -2
        d = defaultdict(int)

        for x in 'J23456789TQKA':
            d = defaultdict(int)
            for c in hand:
                d[c] += 1
            if x != "J":
                d[x] = d[x] + d['J']
                del d["J"]
            if max(d.values()) == 5 and rank < 5:
                rank = 5
            elif max(d.values()) == 4 and rank < 4:
                rank = 4
            elif max(d.values()) == 3 and rank < 3 and min(d.values()) == 2:
                rank = 3
            elif max(d.values()) == 3 and rank < 2:
                rank = 2
            elif list(d.values()).count(2) == 2 and rank < 1:
                rank = 1
            elif list(d.values()).count(2) == 1 and rank < 0:
                rank = 0
            else:
                if rank < -1:
                    rank = -1
        hands[rank].append(hand)

    placements = []
    cardrankings = {"K": 13, "Q": 12, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "A": 14, "J": 1}

    for key in range(-1, 6):
        grouping = hands[key]
        grouping.sort(key=lambda x: [cardrankings[char] for char in x], reverse=True)
        grouping.reverse()
        for i in grouping:
            placements.append(i)
    total = 0

    for i, h in enumerate(placements):
        total += (i+1) * bids[h]
    return total
contents = open("day7.txt").read().splitlines()
print(star1())
print(star2())
