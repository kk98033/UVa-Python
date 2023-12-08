''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10415 - Eb Alto Saxophone Player
def solve(codes):
    dict = {
        'c': '0111001111',
        'd': '0111001110',
        'e': '0111001100',
        'f': '0111001000',
        'g': '0111000000',
        'a': '0110000000',
        'b': '0100000000',
        'C': '0010000000',
        'D': '1111001110',
        'E': '1111001100',
        'F': '1111001000',
        'G': '1111000000',
        'A': '1110000000',
        'B': '1100000000',
    }
    current = '0000000000'
    ans = [0] * 10
    for code in codes:
        hold = dict[code]
        for i in range(10):
            if current[i] == '0' and hold[i] == '1':
                ans[i] += 1
        current = hold

    return ' '.join(map(str, ans))

T = int(input())
for t in range(T):
    codes = input()
    print(solve(codes))