''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n, nums):
    sums = []
    for i in range(n):
        for j in range(i, n):
            sums.append(nums[i] + nums[j])
    return 'It is a B2-Sequence.' if len(sums) == len(set(sums)) else 'It is not a B2-Sequence.'

count = 1
while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        print(f'Case #{count}: {solve(n, nums)}')
        count += 1
    except EOFError:
        break