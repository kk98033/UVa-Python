''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n, nums):
    mid = sum(nums) // 2
    dp = [[0 for i in range(mid)] for j in range(n+1)]
    for i in range(n + 1):
        for j in range(mid):
            print(i, j)
            if nums[i-1] < mid:
                dp[i][j] = max(nums[i-1] + dp[i-1][mid-nums[i-1]], dp[i-1][nums[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp

T = int(input())
for t in range(T):
    n = int(input())
    nums = list(map(int, input().split()))

    print(solve(n, nums))