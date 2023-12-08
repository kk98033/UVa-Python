''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def dfs(n, nums, cur, result):
    print(cur, nums)
    result.append(cur)
    for i in range(n):
        dfs(n-1, nums[0:i]+nums[i+1:], cur + [nums[i]], result)
    return


def solve(target, n, nums):
    result = []
    dfs(n, nums, [], result)
    print('a', result)
    return target, n, nums

T = int(input())
for t in range(T):
    target = int(input())
    n = int(input())
    nums = list(map(int, input().split()))

    print(solve(target, n, nums))
    # print(f'Case #{T+1}: {solve(n)}')