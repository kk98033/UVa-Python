''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

import sys

def solve(n, p, q, nums1, nums2):
    dp = [[0] * (q+2) for _ in range(p+2)]
    positions = [-1] * (n*n + 1)

    for j in range(1, q+1):
        positions[nums2[j]] = j

    lis_len = 0
    for i in range(1, p+1):
        if positions[nums1[i]] != -1:
            pos = positions[nums1[i]]
            for j in range(1, lis_len+1):
                if dp[j-1][pos-1] < i and dp[j][pos] > i:
                    dp[j][pos] = i
            else:
                dp[lis_len+1][pos] = i
                lis_len = max(lis_len+1, j)

    return lis_len

T = int(sys.stdin.readline())
for t in range(T):
    n, p, q = map(int, sys.stdin.readline().split())
    nums1 = [0] + list(map(int, sys.stdin.readline().split()))
    nums2 = [0] + list(map(int, sys.stdin.readline().split()))

    print(f'Case {t+1}: {solve(n, p, q, nums1, nums2)}')
