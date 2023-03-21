''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10019 - Funny Encryption Method
def solve(n):
    # https://stackoverflow.com/questions/9210525/how-do-i-convert-hex-to-decimal-in-python
    n_2 = f'{n:b}'.count('1')
    n_16 = f'{int(str(n), 16):b}'.count('1')

    return f'{n_2} {n_16}'

T = int(input())
for t in range(T):
    n = int(input())
    print(solve(n))
# Accepted	PYTH3	0.010