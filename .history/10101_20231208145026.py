''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n):
    # 'kuti' (10000000), 'lakh' (100000), 'hajar' (1000), 'shata' (100) 
    result = ""
    if n >= 10000000:
        result += f' {solve(n // 10000000)} kuti'
        n = n % 10000000
    if n >= 100000:
        result += f' {solve(n // 100000)} lakh'
        n = n % 100000
    if n >= 1000:
        result += f' {solve(n // 1000)} hajar'
        n = n % 1000
    if n >= 100:
        result += f' {solve(n // 100)} shata'
        n = n % 100
    if n != 0:
        result += f'{str(n)} '

    return result

count = 1
while True:
    try:
        n = int(input())
        ans = solve(n)
        if ans and ans[-1] == " ": ans = ans[:-1]
        print(f'{count:>4}. {ans}')
        count += 1
    except EOFError:
        break