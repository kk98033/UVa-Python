''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(m, n):
    if m == 0 or n == 0: return 'Boring!' 
    if m == 1 and n == 1: return 'Boring!'
    ans = [m]
    while m > 1:
        if m % n != 0: return 'Boring!'
        ans.append(m // n)
        m //= n
    return ' '.join([str(i) for i in ans])

def solve(m, n):
    if m == 0 or n == 0: return 'Boring!' 
    if m == 1 and n == 1: return 'Boring!'
    ans = f'{m}'
    while m > 1:
        if m % n != 0: return 'Boring!'
        ans += f' {m // n}'
        m //= n
    return ' '.join([str(i) for i in ans])

# UVa 10190 - Divide, But Not Quite Conquer!
while True:
    try:
        m, n = list(map(int, input().split()))

        print(solve2(m, n))
    except EOFError:
        break