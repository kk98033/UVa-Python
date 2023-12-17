''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 392 - Polynomial Showdown
# = = 這題有夠煩，懶得想要怎麼寫比較好了
def solve(nums):
    start = False
    ans = []
    
    for i, n in enumerate(nums):
        power = 9 - i - 1
        if n != 0 and not start: 
            start = True
            
            if n == 1 and power != 0: 
                n = ''
            elif n == -1 and power != 0:
                n = '-'
                
            if power > 1:
                ans.append(f'{ n }x^{ power }')
            elif power == 1:
                ans.append(f'{ n }x')
            elif power == 0:
                ans.append(f'{ n }')
        elif start:
            if n == 0: continue

            if n > 0:
                ans.append('+')
            elif n < 0:
                ans.append('-')

            if abs(n) == 1 and power != 0: 
                n = ''
            else:
                n = abs(n)

            if power > 1:
                ans.append(f'{ n }x^{ power }')
            elif power == 1:
                ans.append(f'{ n }x')
            else:
                ans.append(f'{ n }')

    if not start: return 0
                
    return ' '.join(ans)

while True:
    try:
        nums = list(map(int, input().split()))

        print(solve(nums))
    except EOFError:
        break
# Accepted	PYTH3	1.370