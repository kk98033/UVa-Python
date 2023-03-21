''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10268 - 498-bis
def solve(x, nums):
    if len(nums) < 2: return 0
    ans = nums[-2]
    # for i in range(len(nums)-3, -1, -1):
    #     ans += nums[i] * (len(nums) - i - 1) * pow(x, (len(nums) - i - 1 - 1))
    for i in range(len(nums)-2):
        ans += nums[i] * (len(nums) - i - 1) * pow(x, (len(nums) - i - 1 - 1))
    return ans

while True:
    try:
        x = int(input())
        nums = list(map(int, input().split()))

        print(solve(x, nums))
    except EOFError:
        break
# Time limit exceeded	PYTH3	3.000 WTF DUDE???