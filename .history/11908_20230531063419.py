''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 11908 - Skyscraper
import sys
def solve(n, nums):
    # maxLen = max([i[0] + i[1] - 1 for i in nums])
    maxList = max(nums, key=lambda x: x[0] + x[1] - 1)
    maxLen = maxList[0] + maxList[1] - 1
    dp = [0] * (maxLen + 1)
    nums.sort(key=lambda x: x[0] + x[1] - 1)

    index = 1
    for start, end, price in nums:
        while index < start + end - 1:
            dp[index] = max(dp[index-1], dp[index]) 
            index += 1
        if start == 0:
            dp[start+end-1] = max(price, dp[start+end-2], dp[start+end-1])
        else:
            dp[start+end-1] = max(dp[start-1] + price, dp[start+end-2], dp[start+end-1])
    return dp[-1]

T = int(input())
for t in range(T):
    n = int(input())
    nums = []
    for i in range(n):
        # nums.append(list(map(int, input().split())))
        nums.append(list(map(int, sys.stdin.readline().split())))
    print(f'Case {t+1}: {solve(n, nums)}')
# Accepted	PYTH3	1.440