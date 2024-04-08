''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa UVa 10783 - Odd Sum
def solve(n1, n2):
    ans = 0
    for i in range(n1, n2+1):
        if i % 2 != 0:
            ans += i
    return ans

def solve2(a, b):
    # 確保首項和末項都是奇數
    if a % 2 == 0: a += 1
    if b % 2 == 0: b -= 1
    
    # 計算 a 到 b 之間奇數的數量
    n = (b - a) // 2 + 1
    
    # 使用等差數列的求和公式
    total = n * (a + b) // 2
    return total

T = int(input())
for t in range(T):
    n1 = int(input())
    n2 = int(input())
    
    print(f'Case {t+1}: {solve(n1, n2)}')
# Accepted	PYTH3	0.020