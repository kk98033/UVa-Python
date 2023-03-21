''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n, ans):
    # 'kuti' (10000000), 'lakh' (100000), 'hajar' (1000), 'shata' (100) 
    if n >= 10000000:
        ans['kuti'] += 1
        ans = solve(n - 10000000, ans)
    elif n >= 100000:
        ans['lakh'] += 1
        ans = solve(n - 100000, ans)
    elif n >= 1000:
        ans['hajar'] += 1
        ans = solve(n - 1000, ans)
    elif n >= 100:
        ans['shata'] += 1
        ans = solve(n - 100, ans)
    else:
        ans[''] += n
    return ans

while True:
    try:
        n = int(input())

        print(solve(n, { 'kuti': 0, 'lakh': 0, 'hajar': 0, 'shata': 0, '': 0 }))
    except EOFError:
        break