''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

'''
1. input n
2. print n
3. if n = 1 then STOP
4. if n is odd then n ←− 3n + 1
5. else n ←− n/2
6. GOTO 2
'''

appeared = {}

def solve(i, j):
    count = ans = 0
    for cur in range(min(i, j), max(i, j)+1):
        count = 0
        n = cur
        while True:
            if n in appeared: 
                count += appeared[n]
                break

            count += 1
            if n == 1: break
            if n % 2 != 0: n = 3 * n + 1
            else: n = n // 2
        
        # print(cur)
        appeared[cur] = count
        # print(appeared)
        ans = max(count, ans)

    return f'{i} {j} {ans}'

while True:
    try:
        i, j = list(map(int, input().split()))
        print(solve(i, j))
    except EOFError:
        break