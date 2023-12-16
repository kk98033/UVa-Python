''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 11121 - Base -2
def solve(n):
    if n == 0:
        return '0'

    result = ''
    while n != 0:
        remainder = n % -2

        n = n // -2

        if remainder < 0:
            remainder += 2
            n += 1

        result = str(remainder) + result

    return result

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    result = solve(n)
    print(f"Case #{i}:", '0' if result == '' else result)
# Accepted	PYTH3	0.230