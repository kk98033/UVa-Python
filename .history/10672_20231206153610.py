''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10672 - Marbles on a tree
def dfs(node, parent):
    marbles_needed = 1 - marbles[node]
    moves = 0

    for child in tree[node]:
        if child != parent:
            child_moves, child_marbles = dfs(child, node)
            marbles_needed += child_marbles
            moves += child_moves

    return moves + abs(marbles_needed), marbles_needed

while True:
    try:
        n = int(input().strip())
        if n == 0:
            break

        tree = [[] for _ in range(n + 1)]
        marbles = [0] * (n + 1)

        for _ in range(n):
            data = list(map(int, input().split()))
            node = data[0]
            marbles[node] = data[1]
            children = data[3:]
            for child in children:
                tree[node].append(child)
                tree[child].append(node)
        print(marbles)
        root = 1  # 假設 1 號節點是根節點
        total_moves, _ = dfs(root, -1)
        print(total_moves)
    except:
        break
