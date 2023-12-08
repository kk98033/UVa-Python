''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}



def solve(target, n, nums):
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

def solve2(target, n, nums):
    dp = [False] * (target + 1)
    dp[0] = True
    for bar in nums:
        for i in range(target, -1, -1):
            if dp[i] and bar + i <= target:
                dp[bar + i] = True
    return dp

    def is_possible(target, bars):
        n = len(bars)
        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(n):
            for j in range(target, -1, -1):
                if dp[j] and j + bars[i] <= target:
                    dp[j + bars[i]] = True

        return dp[target]

    if is_possible(target, nums):
        return "YES"
    else:
        return "NO"



T = int(input())
for t in range(T):
    target = int(input())
    n = int(input())
    nums = list(map(int, input().split()))

    # print(solve(target, n, nums))
    print(solve2(target, n, nums))