''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n, nums):
    nums.sort()
    mid = n // 2
    different  = [abs(nums[mid] - i) for i in nums]
    if n % 2 == 0:
        different2 = [abs(nums[mid-1] - i) for i in nums]
        if sum(different) < sum(different2):
            return f'{nums[mid]} {different.count(min(different))} 1'
        else:
            return f'{nums[mid-1]} {different2.count(min(different2))} 1'
    return f'{nums[mid]} {different.count(min(different))} 1'

while True:
    try:
        n = int(input())
        nums = []
        for i in range(n):
            nums.append(int(input()))

        print(solve(n, nums))
    except EOFError:
        break