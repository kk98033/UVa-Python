''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10672 - Marbles on a tree
def dfs(node, parent):
    needed = 1 - marbles[node] # 這個節點還差多少才能滿足只有一個珠珠(可正可負)
    moves = 0

    for child in trees[node]:
        if child != parent: # 避免重複遍歷，導致遞迴出不去
            childMoves, childNeeded = dfs(child, node)
            needed += childNeeded # 累加子節點需要從父節點接收或給予的珠珠數（因為珠珠要移動到子節點時一定會經過父節點）
            moves += childMoves # 紀錄總共的移動次數（這是因為無論是給予還是接收彈珠，都算作一次移動）

    return moves + abs(needed) , needed 

while True:
    try:
        n = int(input())
        if n == 0: break

        trees = [[] for _ in range(n + 1)] # 用二維陣列來存取樹
        marbles = [0] * (n + 1)

        for _ in range(n):
            temp = list(map(int, input().split()))
            trees[temp[0]].extend(temp[3:])
            for child in temp[3:]: # 在子節點中紀錄他的父節點(方便遍歷所有樹的節點)
                trees[child].append(temp[0])
            marbles[temp[0]] = temp[1]

        ans, _ = dfs(1, -1) # 先假設節點1是跟節點，他沒有父節點(-1)
        print(ans)

    except EOFError:
        break
# Accepted	PYTH3	0.270


# def dfs(node, parent):
#     marbles_needed = 1 - marbles[node]
#     moves = 0

#     for child in tree[node]:
#         if child != parent:
#             child_moves, child_marbles = dfs(child, node)
#             marbles_needed += child_marbles
#             moves += child_moves

#     return moves + abs(marbles_needed), marbles_needed

# while True:
#     try:
#         n = int(input().strip())
#         if n == 0:
#             break

#         tree = [[] for _ in range(n + 1)]
#         marbles = [0] * (n + 1)

#         for _ in range(n):
#             data = list(map(int, input().split()))
#             node = data[0]
#             marbles[node] = data[1]
#             children = data[3:]
#             for child in children:
#                 tree[node].append(child)
#                 tree[child].append(node)
#         print(marbles)
#         print(tree)
#         root = 1  # 假設 1 號節點是根節點
#         total_moves, _ = dfs(root, -1)
#         print(total_moves)
#     except:
#         break
