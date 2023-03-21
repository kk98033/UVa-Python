''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(s, d):
    days = 1
    cur = s
    while days + s <= d:
        cur += 1
        days += cur
    return cur

def solve2(s, d):
    return (-1 + (1 - 4 * ((s ** 2 + s - 2 * d) ** 0.5))) * 0.5

while True:
    try:
        s, d = list(map(int, input().split()))
        print(solve(s, d))
    except EOFError:
        break