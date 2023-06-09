''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10922 - 2 the 9s
def solve(n):
    degree = 0
    temp = list(map(int, n))
    while True:
        # print(n)
        sums = sum(temp)
        if sums % 9 == 0:
            temp = list(map(int, str(sums)))
            degree += 1
        else:
            return f'{n} is not a multiple of 9.'
        
        if len(temp) == 1: break # for '9'

    return f'{n} is a multiple of 9 and has 9-degree {degree}.'

while True:
    try:
        n = input()
        if n == '0': break
        print(solve(n))
    except EOFError:
        break
# Accepted	PYTH3	0.390