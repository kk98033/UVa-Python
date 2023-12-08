''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10242 - Fourth Point !!
def solve(p1, p2, p3, p4):
    if p1 == p2 or p1 == p3 or p1 == p4: mid = p1
    elif p2 == p1 or p2 == p3 or p2 == p4: mid = p2
    elif p3 == p1 or p3 == p2 or p3 == p4: mid = p3
    else: mid = p4

    points = [p1, p2, p3, p4]
    points.remove(mid)
    points.remove(mid)
    a, b, c = points[0], mid, points[1]

    '''
    b ____ C
     /___/
    a     
    '''

    o = ((a[0] + c[0]) / 2, (a[1] + c[1]) / 2)
    return f'{round(2 * o[0] - b[0], 3):.3f} {round(2 * o[1] - b[1], 3):.3f}'

while True:
    try:
        points = list(map(float, input().replace('−', '-').split())) # bruh wtf
        print(solve((points[0:2]), (points[2:4]), (points[4:6]), (points[6:8])))
    except EOFError:
        break