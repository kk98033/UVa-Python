''' 3 '''
''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n):
    return



from collections import defaultdict

from collections import defaultdict

def dfs(graph, node, parent, dist, distances):
    for neighbor, weight in graph[node]:
        if neighbor != parent:
            distances[neighbor] = dist + weight
            dfs(graph, neighbor, node, distances[neighbor], distances)

def findCentralNode(tree_nodes, tree_from, tree_to, tree_weight, x, y, z):
    graph = defaultdict(list)
    # Constructing the undirected graph
    for i in range(len(tree_from)):
        graph[tree_from[i]].append((tree_to[i], tree_weight[i]))
        graph[tree_to[i]].append((tree_from[i], tree_weight[i]))
    
    # Initialize distances from X, Y, Z to all other nodes as infinity
    dist_from_x = [float('inf')] * (tree_nodes + 1)
    dist_from_y = [float('inf')] * (tree_nodes + 1)
    dist_from_z = [float('inf')] * (tree_nodes + 1)
    
    # Perform DFS from X, Y, Z to calculate the distances
    dist_from_x[x] = 0
    dist_from_y[y] = 0
    dist_from_z[z] = 0
    dfs(graph, x, -1, 0, dist_from_x)
    dfs(graph, y, -1, 0, dist_from_y)
    dfs(graph, z, -1, 0, dist_from_z)

    # Find the central node with the minimal sum of distances to X, Y, and Z
    min_distance_sum = float('inf')
    central_node = -1
    for node in range(1, tree_nodes + 1):
        # Since we initialized distances as infinity, nodes not reachable from X, Y, or Z will not affect the result
        distance_sum = dist_from_x[node] + dist_from_y[node] + dist_from_z[node]
        if distance_sum < min_distance_sum:
            min_distance_sum = distance_sum
            central_node = node
        elif distance_sum == min_distance_sum and node < central_node:
            central_node = node

    return central_node


while True:
    try:
        tree_nodes, tree_edges =  map(int, input().rstrip().split())
        tree_from = [0] * tree_edges
        tree_to = [0] * tree_edges
        tree_weight = [0] * tree_edges

        for i in range(tree_edges):
            tree_from[i], tree_to[i], tree_weight[i] = map(int, input().rstrip().split())
        x = int(input().strip())

        y = int(input().strip())

        z = int(input().strip())
        result = findCentralNode(tree_nodes, tree_from, tree_to, tree_weight, x, y, z)
        print(result)
    except EOFError:
        break

'''
5 4
1 2 15
1 3 10
2 4 20
2 5 25
2
3
4

2
'''