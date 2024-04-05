''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def can_form_lying_graph(edges):
    if len(edges) == 1: return 'Yes'
    # 將邊轉換成頂點之間的對應關係
    edge_to_vertex = {}
    for edge in edges:
        start, end = map(int, edge.split())
        if start not in edge_to_vertex:
            edge_to_vertex[start] = set()
        edge_to_vertex[start].add(end)

    # 檢查每一個頂點uv是否有對應的vw
    for start in edge_to_vertex:
        for end in edge_to_vertex[start]:
            if end not in edge_to_vertex:
                return "No"
            if not edge_to_vertex[start].issubset(edge_to_vertex[end]):
                return "No"
    return "Yes"

# 讀取測試案例數量
t = int(input().strip())
results = []

for case_number in range(1, t + 1):
    m = int(input().strip())
    k = int(input().strip())
    edges = [input().strip() for _ in range(k)]

    result = can_form_lying_graph(edges)
    results.append(f"Case #{case_number}: {result}")

# 輸出結果
for result in results:
    print(result)
    


'''
def solve(m, k, tree, nodes):
    if len(tree) <= 1: return 'Yes'
    walked = set()
    def dfs(parent, children):
        # print(parent)
        if not children:
            return
        
        if len(walked) >= len(nodes):
            return

        walked.add(parent)

        for child in children:
            # print(child)
            if child in tree and child not in walked and child != parent:
                dfs(child, tree[child])

        return
    # dfs(tree[0], tree)
    # print(tree)
    head = list(nodes)[0]
    dfs(head, tree[head])
    # print(tree, head, tree[head])
    # print(walked)
    return 'Yes' if len(walked) >= len(nodes) else 'No' 

T = int(input())
for t in range(T):
    m = int(input())
    k = int(input())
    tree = {}
    nodes = set()
    for _ in range(k):
        node, child = map(int, input().split())
        if node in tree:
            tree[node].add(child)
            # tree[node].add(node)
        else:
            tree[node] = {child}
            # tree[node] = {node}
        
        # tree[node] = tree.get(node, []) + [child, node]

        nodes.add(node)

    print(f'Case #{t+1}: {solve(m, k, tree, nodes)}')
    '''