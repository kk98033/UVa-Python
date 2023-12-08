''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n, p, q, nums1, nums2):
    dp = [[0 for j in range(q+2)] for i in range(p+2)]
    for i in range(1, p+2):
        for j in range(1, q+2):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    for i in dp:
        print(i)
    return n, p, q, nums1, nums2

T = int(input())
for t in range(T):
    n, p, q = list(map(int, input().split()))
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    print(solve(n, p, q, nums1, nums2))