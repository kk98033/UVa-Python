''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa - 11240 - Antimonotonicity
# 2023/03/21/ CPE - 4
def solve(n, nums):
    wave = [1] * n
    current = 1 
    ans = 0
    for i in range(1, n):
        if current == 1:
            if nums[i-1] - nums[i] > 0: 
                ans += 1
                current *= -1
        else:
            if nums[i-1] - nums[i] < 0: 
                ans += 1
                current *= -1
    return ans

T = int(input())
for t in range(T):
    nums = list(map(int, input().split()))

    print(solve(nums[0], nums[1:]))