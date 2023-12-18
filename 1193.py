''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# 1193 - Radar Installation
def solve(n, nums):
    intervals = []
    for x, y in nums:
        if y > d: return -1
        # d = ((x-a)^2 + (y-0)^2) ^ 0.5
        # d^2 = (x-a)^2 + (y-0)^2
        # x - a = +- (d^2 - (y-0)^2) ^ 0.5
        # a = x +- (d^2 - (y-0)^2) ^ 0.5
        base = (d ** 2 - y ** 2) ** 0.5
        intervals.append((x - base, x + base))
    intervals.sort(key=lambda x: x[1])

    ans = 0
    covered = -float('inf')
    for start, end in intervals:
        if start > covered:
            covered = end
            ans += 1

    return ans

t = 1
while True:
    try:
        n, d = list(map(int, input().split()))
        if (n, d) == (0, 0): break
        nums = [list(map(int, input().split())) for _ in range(n)]
        temp = input()
        print(f'Case {t}: {solve(n, nums)}')
        t += 1
    except EOFError:
        break
# Accepted	PYTH3	0.080