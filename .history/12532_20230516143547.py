''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n, k, nums, codes):
    nums = [1 if i > 0 else -1 for i in nums]
    for code, n1, n2 in codes:
        if code == 'C':
            nums[int(n1)-1] = 1 if int(n2) > 0 else -1
        elif code == 'P':
            if 0 in nums[int(n1)-1:int(n2)]: print(0)
            else:
                print('+' if nums[int(n1)-1:int(n2)].count(-1) % 2 == 0 else '-')
    return nums

while True:
    try:
        n, k = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        codes = []
        for i in range(k):
            codes.append(input().split())

        print(solve(n, k, nums, codes))
    except EOFError:
        break