''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 11824 - A Minimum Land Price
# 2023/03/21/ CPE - 2
def solve(nums):
    nums = sorted(nums)[::-1]
    ans = 0
    for i, value in enumerate(nums):
        ans += 2 * (value ** (i + 1))
    return ans if ans < 5000000 else 'Too expensive'

T = int(input())
nums = []
for _ in range(T):
    nums = []
    while True:
        temp = int(input())
        if temp == 0: 
            print(solve(nums))
            break
        nums.append(temp)
# Accepted	PYTH3	0.040