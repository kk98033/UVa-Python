''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10193 - All You Need Is Love
import math
def solve(s, l):
    s, l = int(s, 2), int(l, 2)
    if math.gcd(s, l) > 1:
        return 'All you need is love!'
    return 'Love is not all you need!'

T = int(input())
for t in range(T):
    s = input()
    l = input()
    print(f'Pair #{t+1}: {solve(s, l)}')
# Accepted	PYTH3	0.050