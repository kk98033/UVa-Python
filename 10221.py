''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10221 - Satellites
'''
chord formula: https://flexbooks.ck12.org/cbook/ck-12-trigonometry-concepts/section/2.7/primary/lesson/length-of-a-chord-trig/
arc formula: https://byjus.com/arc-length-formula/
'''
import math
def solve(s, a, d):
    r = 6440 # earth radius

    if d == 'min': a /= 60
    if a > 180: a = abs(360 - a)

    rad = math.pi / 180 * a
    arc = (r + s) * rad
    chord = 2 * (r + s) * math.sin(rad / 2)
    return f'{round(arc, 6):.6f} {round(chord, 6):.6f}' # https://stackoverflow.com/questions/19986662/rounding-a-number-in-python-but-keeping-ending-zeros

while True:
    try:
        s, a, d = input().split()

        print(solve(int(s), int(a), d))
    except EOFError:
        break
# Accepted	PYTH3	0.090