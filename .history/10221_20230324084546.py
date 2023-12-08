''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

import math
def solve(r, a, d):
    # if d == 'min': a /= 60
    return (r ** 2 + r ** 2 - 2 * r * r * math.cos(a)) ** 0.5, 2 * r * math.sin((math.pi / 180 * a) / 2)

while True:
    try:
        r, a, d = input().split()

        print(solve(int(r), int(a), d))
    except EOFError:
        break