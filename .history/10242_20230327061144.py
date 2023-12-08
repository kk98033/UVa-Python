''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10242 - Fourth Point !!
def solve(p1, p2, p3, p4):
    return p1, p2, p3, p4

T = int(input())
for t in range(T):
    (p1), (p2), (p3), (p4) = list(map(int, input().split()))

    print(solve(p1, p2, p3, p4))
    # print(f'Case #{T+1}: {solve(n)}')