''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import deque
import sys
input = sys.stdin.read

# UVa 11518 - Dominos 2
def solve(n, m, l, graph, initial_knocked):
    stack = deque()
    visited = set()
    
    for k in initial_knocked:
        stack.append(k)
        while stack:
            cur = stack.pop()
            if cur not in visited:
                visited.add(cur)
                if cur in graph:
                    stack.extend(graph[cur])
    
    return len(visited)

data = input().split()
index = 0
T = int(data[index])
index += 1

results = []

for _ in range(T):
    n = int(data[index])
    m = int(data[index + 1])
    l = int(data[index + 2])
    index += 3
    
    graph = {}
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        index += 2
    
    initial_knocked = []
    for _ in range(l):
        initial_knocked.append(int(data[index]))
        index += 1
    
    results.append(solve(n, m, l, graph, initial_knocked))

for result in results:
    print(result)
