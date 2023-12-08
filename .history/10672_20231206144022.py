''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10672 - Marbles on a tree
def dfs(node, parent, moves):
    total_marbles = marbles[node] - 1  # 當前節點的彈珠數量減 1（因為我們希望每個節點最終都只有一個彈珠）
    for child in tree[node]:
        if child != parent:
            moves, child_marbles = dfs(child, node, moves)
            total_marbles += child_marbles
    moves += abs(total_marbles)  # 累加移動次數
    return moves, total_marbles  # 返回更新後的移動次數和這個節點的彈珠變化量

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

    moves, _ = dfs(1, -1, 0)
    print(moves)
