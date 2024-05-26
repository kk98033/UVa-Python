''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 11518 - Dominos 2
def solve(n, m, l, graph, initial_knocked):
    stack = []
    visited = set()
    for k in initial_knocked:
        stack.append(k)
        while stack:
            cur = stack.pop(0)
            if cur not in visited:
                visited.add(cur)
                if cur in graph:
                    stack.extend(graph[cur])
    return len(visited)

T = int(input())
for t in range(T):
    n, m, l = list(map(int, input().split()))

    graph = {}
    for _ in range(m):
        key, value = list(map(int, input().split()))
        graph[key] = graph.get(key, []) + [value]

    initial_knocked = []
    for _ in range(l):
        initial_knocked.append(int(input()))

    print(solve(n, m, l, graph, initial_knocked))
# Accepted	PYTH3	1.360