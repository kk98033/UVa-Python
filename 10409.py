''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10409 - Die Game
def solve(codes):
    # "east"、"south"、"west"、"north"。
    '''
           2
        3  1  4  6
           5
    '''
    north, west, top = 2, 3, 1
    for code in codes:
        if code == 'east':
            north, west, top = north, 7 - top, west
        elif code == 'south':
            north, west, top = 7 - top, west, north
        elif code == 'west':
            north, west, top = north, top, 7 - west
        else: # north
            north, west, top = top, west, 7 - north
    return top

while True:
    try:
        n = int(input())
        if n == 0: break

        codes = []
        for _ in range(n):
            codes.append(input())

        print(solve(codes))
    except EOFError:
        break
# Accepted	PYTH3	0.020