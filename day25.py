from collections import defaultdict, deque
import random
from copy import deepcopy


def contract(graph, u, v):
    combined_node = u + v
    graph[combined_node] = graph[u] + graph[v]
    del graph[u]
    del graph[v]
    for node, edges in graph.items():
        graph[node] = [combined_node if x == u or x == v else x for x in edges]
        graph[node] = [x for x in graph[node] if x != node]


def karger_min_cut(graph):
    while len(graph) > 2:
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])
        contract(graph, u, v)
    return len(graph[list(graph.keys())[0]]), graph


def star1():
    wires = defaultdict(lambda: list())
    for line in contents:
        line = line.split(": ")
        source = line[0]
        for wire in line[1].split(" "):
            wires[wire].append(source)
            wires[source].append(wire)

    copyWires = deepcopy(wires)
    c, cuts = karger_min_cut(copyWires)
    while c != 3:
        copyWires = deepcopy(wires)
        c, cuts = karger_min_cut(copyWires)
    total = 1
    for name in cuts.keys():
        total *= len(name) // 3
    return total

contents = open('day25.txt').read().splitlines()
print(star1())
