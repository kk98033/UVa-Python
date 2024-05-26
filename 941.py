''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

# UVa 941 - Permutations
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def solve(n, s):
    s = sorted([i for i in s])
    temp = n
    len_of_s = len(s)
    ans = ''
    while s:
        temp_factorial = factorial(len_of_s - 1)
        len_of_s -= 1
        index = temp // temp_factorial
        ans += s.pop(index)
        temp %= temp_factorial
    return ans

T = int(input())
for t in range(T):
    s = input()
    n = int(input())

    print(solve(n, s))
# Accepted	PYTH3	2.210