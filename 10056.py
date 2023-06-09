''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# 10056 - What is the Probability ?
def solve(n, p, target):
    if p == 0: return f'{0:.4f}'
    q = (1 - p)
    return f'{p * (q ** (target - 1) / (1 - q ** n)):.4f}'

T = int(input())
for t in range(T):
    n, p, target = input().split()
    print(solve(int(n), float(p), int(target)))
# Accepted	PYTH3	0.010