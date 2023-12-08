''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10672 - Marbles on a tree
def dfs(node, parent):
    total_moves = 0
    total_marbles = marbles[node] - 1  # 節點自己的彈珠數量 - 1，因為目標是每個節點剩下一個彈珠

    for child in tree[node]:
        if child != parent:
            moves_from_child = dfs(child, node)
            total_marbles += moves_from_child
            total_moves += abs(moves_from_child)

    return total_moves + abs(total_marbles)

while True:
    n = int(input().strip())
    if n == 0:
        break

    tree = [[] for _ in range(n + 1)]
    marbles = [0] * (n + 1)

    for _ in range(n):
        data = list(map(int, input().split()))
        node = data[0]
        marbles[node] = data[1]
        tree[node].extend(data[3:])

    print(dfs(1, -1))
