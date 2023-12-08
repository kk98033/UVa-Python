''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 11417 - GCD
import math
def solve(n):
    g = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            g += math.gcd(i, j)
            # g += gcd(i, j)
    return g

def gcd(a, b):
    # Accepted	PYTH3	1.410
    while b:
        a, b = b, a % b
    return a

while True:
    try:
        n = int(input())
        if n == 0: break

        print(solve(n))
    except EOFError:
        break
# Accepted	PYTH3	0.820