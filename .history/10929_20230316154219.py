''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n):
    return f'{n} is a multiple of 11.' if abs(sum([int(i) for i in n[0::2]]) - sum([int(i) for i in n[1::2]])) % 11 == 0 else f'{n} is not a multiple of 11.'

def solve2(n):
    return f'{n} is a multiple of 11.' if n % 11 == 0 else f'{n} is not a multiple of 11.'

while True:
    try:
        n = input()
        if n == '0': break
        print(solve(n))
    except EOFError:
        break