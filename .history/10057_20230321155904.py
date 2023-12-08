''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10057 - A mid-summer night's dream.
def solve(n, nums):
    nums.sort()
    mid1, mid2 = n // 2, n // 2 - 1
    different1  = [abs(nums[mid1] - i) for i in nums]
    different2 = [abs(nums[mid2] - i) for i in nums]
    if n % 2 == 0:
        return f'{min(nums[mid1], nums[mid2])} {nums.count(nums[mid1] + nums.count(mid2))} {nums[mid1] - nums[mid2] + 1}'
        if sum(different1) < sum(different2):
            return f'{nums[mid1]} {different1.count(0) + different2.count(0)} {nums[mid1] - nums[mid2] + 1}'
        else:
            print(sorted(different2))
            print(sorted(different1))
            return f'{nums[mid2]} {different1.count(0) + different2.count(0)} {nums[mid1] - nums[mid2] + 1}'
    return f'{nums[mid1]} {nums.count(nums[mid1] + nums.count(mid2))} 1'

while True:
    try:
        n = int(input())
        nums = []
        for i in range(n):
            nums.append(int(input()))

        print(solve(n, nums))
    except EOFError:
        break