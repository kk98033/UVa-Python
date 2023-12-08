''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 13055 - Inception
# 2023/03/21/ CPE - 3
def solve(n, codes):
    dream = []
    for code in codes:
        if code[0] == 'Sleep':
            dream.append(code[1])
        elif code[0] == 'Test':
            if dream:
                print(dream[-1])
            else:
                print('Not in a dream')
        elif code[0] == 'Kick':
            if dream:
                dream.pop()

n = int(input())
while True:
    try:
        codes = []
        for i in range(n):
            codes.append(input().split())
        solve(n, codes)
    except EOFError:
        break
# Accepted	PYTH3	0.160