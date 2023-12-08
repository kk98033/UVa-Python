''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n, nums):
    # maxLen = max(max(nums, key=lambda x: x[0] + x[1]))
    maxLen = max([i[0] + i[1] for i in nums])
    dp = [0] * (maxLen)
    nums.sort()
    # print(maxLen, nums)
    index = 1
    for start, end, price in nums:
        while index < start + end:
            dp[index] = max(dp[index-1], dp[index]) 
            index += 1
        # print('a', dp)
        # if start == 0:
        #     dp[start+end-1] = max(dp[start] + price, dp[start+end-2], dp[start+end-1])
        # else:
        dp[start+end-1] = max(dp[start-1] + price, dp[start+end-2], dp[start+end-1])
        # index = start
        index = start + end
        # if nums == sorted([[1, 8, 2], [0, 9, 6], [0, 6, 8]]):
        #     print(start, end, price, dp[start-1])
        #     print(dp)
        # print(index)

    # while index < maxLen + 1:
    #     dp[index] = max(dp[index-1], dp[index]) 
    #     index += 1

    # print(dp)

    return max(dp)

T = int(input())
for t in range(T):
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(list(map(int, input().split())))
    # if t+1 == 531: print(nums)
    print(f'Case {t+1}: {solve(n, nums)}')