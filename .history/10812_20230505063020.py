''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10812 - Beat the Spread!
def solve(sums, different):
    if different > sums: return 'impossible'

    '''
        x + y = 40
        x - y = 20

        2y = 20
        y = 10
        x = 30
    '''
    y = (sums - different) / 2
    x = (sums - different) / 2 + different

    if not y.is_integer(): # [or isinstance(y, float)]
        return 'impossible' # float
    return f'{int(x)} {int(y)}'

T = int(input())
for t in range(T):
    sums, different = list(map(int, input().split()))
    print(solve(sums, different))
# Accepted	PYTH3	0.040