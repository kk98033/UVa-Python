''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n, nums):
    jollies = sorted([abs(nums[i] - nums[i-1]) for i in range(1, n)])
    for i in range(1, n):
        if jollies[i-1] != i: 
            return 'Not jolly'
    return 'Jolly'

while True:
    try:
        nums = list(map(int, input().split()))
        print(solve(nums[0], nums[1:]))
    except EOFError:
        break