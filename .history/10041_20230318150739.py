''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n, nums):
    nums.sort()
    if len(nums) % 2 != 0: 
        mid = nums[n//2]
        count = 0
        for i in nums:
            count += abs(mid - i)
        return count

    mid1, mid2 = nums[n//2], nums[n//2-1]
    count1 = count2 = 0
    for i in nums:
        count1 += abs(mid1 - i)
        count2 += abs(mid2 - i)
    return min(count1, count2)

def solve2(n, nums):
    nums.sort()
    mid = nums[n//2]
    ans = 0
    for i in nums:
        ans += abs(i - mid)
    return ans

T = int(input())
for t in range(T):
    n = list(map(int, input().split()))
    print(solve2(n[0], n[1:]))

    # print(solve(n[0], n[1:]))