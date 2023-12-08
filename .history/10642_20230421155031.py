''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(x1, y1, x2, y2):
    level_1 = x1 + y1
    startNum_1 = ((1 + (level_1 - 1)) * (level_1 - 1)) // 2
    num_1 = startNum_1 + y1

    level_2 = x2 + y2
    startNum_2 = ((1 + (level_2 - 1)) * (level_2 - 1)) // 2
    num_2 = startNum_2 + y2
    return num_2 - num_1

T = int(input())
for t in range(T):
    x1, y1, x2, y2 = list(map(int, input().split()))
    print(solve(x1, y1, x2, y2))