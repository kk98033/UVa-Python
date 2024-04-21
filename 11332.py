''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 11332 - Summing Digits
def solve(n):
    ans = n
    n = list(map(int, n))
    while len(n) > 1:
        ans = sum(n)
        n = list(map(int, str(ans)))
    return ans

def solve2(n):
    n = int(n)
    if n == 0: return 0
    if n % 9 == 0: return 9
    return n % 9
while True:
    try:
        n = input()
        if n == '0': break
        print(solve2(n))
    except EOFError:
        break
# Accepted	PYTH3	0.020