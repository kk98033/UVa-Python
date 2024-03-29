''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 11934 - Magic Formula
def solve(a, b, c, d, L):
    ans = 0
    for i in range(0, L + 1):
        if ((a * i ** 2) + (b * i) + c) % d == 0:
            ans += 1
    return ans

while True:
    try:
        a, b, c, d, L = list(map(int, input().split())) 
        if (a, b, c, d, L) == (0, 0, 0, 0, 0): break
        print(solve(a, b, c, d, L))
    except EOFError:
        break
# Accepted	PYTH3	0.080