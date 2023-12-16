''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n, k, m):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(1, k+1):
            for x in range(1, min(i, m) + 1):
                dp[i][j] += dp[i-x][j-1]
    return dp[n][k]

while True:
    try:
        n, k, m = list(map(int, input().split()))
        print(solve(n, k, m))
    except EOFError:
        break