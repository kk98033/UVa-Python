''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}


# UVa 12455 - Bars
import itertools
def solve(target, n, nums):
    ''' 暴力法 '''
    def dfs(n, nums, cur, result):
        result.append(cur)

        if n == 0: 
            return
        
        for i in range(len(nums)):
            dfs(n-1, nums[:i], cur + nums[i], result)
        return
        
    result = []
    dfs(n, nums, 0, result)

    return 'YES' if target in result else 'NO'
    # Time limit exceeded	PYTH3	1.000

def solve1(target, n, nums):
    def dfs(nums, cur, result):
        if sum(cur) == target:
            result.append(cur)
            return False

        for i in range(len(nums)):
            res = dfs(nums[i+1:], cur + [nums[i]], result)
            if not res: return False
        return True
    result = []
    dfs()
    return

def solve3(target, n, nums):
    ''' itertools.combinations '''
    for i in range(n+1):
        for subset in itertools.combinations(nums, i):
            if sum(subset) == target:
                return 'YES'
    return 'NO'
    # Accepted	PYTH3	0.010


def solve2(target, n, nums):
    ''' DP '''
    dp = [False] * (target + 1)
    dp[0] = True
    for bar in nums:
        for i in range(target, -1, -1): # 記得從後面開始
            if dp[i] and bar + i <= target:
                dp[bar + i] = True
    return 'YES' if dp[-1] else 'NO'
    # Accepted	PYTH3	0.020

T = int(input())
for t in range(T):
    target = int(input())
    n = int(input())
    nums = list(map(int, input().split()))

    # print(solve(target, n, nums))
    print(solve1(target, n, nums))
    # print(solve2(target, n, nums))
    # print(solve3(target, n, nums))
# Accepted	PYTH3	0.020