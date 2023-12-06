''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

def solve(n, p, q, nums1, nums2):
    dp = [[0] * (q + 1) for _ in range(p + 1)]
    for i in range(1, p + 1):
        for j in range(1, q + 1):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[p][q] + 1

T = int(input())
for t in range(T):
    n, p, q = map(int, input().split())
    nums1 = [0] + list(map(int, input().split()))
    nums2 = [0] + list(map(int, input().split()))
    print(f"Case {t + 1}: {solve(n, p, q, nums1, nums2)}")
