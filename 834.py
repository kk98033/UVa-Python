''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 834 - Continued Fractions
def solve(n1, n2):
    ans = ''
    while n1 >= 1:
        if n1 % n2 == 0:
            ans += f'{n1}'
            break

        ans += f'{n1 // n2},' if ans else f'{n1 // n2};'
        n1, n2 = n2, n1 % n2
    return f'[{ans}]'

while True:
    try:
        n1, n2 = list(map(int, input().split()))
        print(solve(n1, n2))
    except EOFError:
        break
# Accepted	PYTH3	0.020