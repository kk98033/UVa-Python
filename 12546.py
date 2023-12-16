''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 12546 - LCM Pair Sum
MOD = 1000000007
T = int(input())
for t in range(T):
    c = int(input())
    n = ans = 1
    for _ in range(c):
        num, power = list(map(int, input().split()))
        temp = 1
        for i in range(power):
            temp = (temp + num ** (i+1)) % MOD
            n = (n * num) % MOD
        temp = (temp + (num ** power) * power) % MOD
        ans = (ans * temp) % MOD
    ans = (ans + n) % MOD
    print(f"Case { t+1 }: { ans }")
# Accepted	PYTH3	0.230

''' 以下為參考的 code '''

# import math, itertools
# def solve(n, maxN, nums):
#     ans = 0
#     factors = { maxN, 1 }

#     for r in range(1, len(nums) + 1):
#         for combo in itertools.combinations(nums, r):
#             factors.add(math.prod(combo))
#     factors = list(factors)

#     for i in range(len(factors)):
#         for j in range(i, len(factors)):
#             # print(factors[i], factors[j], math.lcm(factors[i], factors[j]))
#             if math.lcm(factors[i], factors[j]) == maxN:
#                 ans += (factors[i] + factors[j])
#                 # print(factors[i], factors[j])
#     return ans % 1000000007

# T = int(input())
# for t in range(T):
#     n = int(input())
#     maxN = 1
#     nums = []
#     for _ in range(n):
#         n1, n2 = list(map(int, input().split()))
#         maxN *= n1 ** n2
#         nums.extend([n1] * n2)
#     # print(nums)
#     print(f'Case {t+1}: {solve(n, maxN, nums)}')



# UVa 12546 - LCM Pair Sum
# MOD = 1000000007

# T = int(input())
# for t in range(T):
#     c = int(input())
#     ans, flag = 1, 1
#     for _ in range(c):
#         a, b = map(int, input().split())
#         fac, tem = 1, 1
#         for _ in range(b):
#             fac = fac * a % MOD
#             tem = (tem + fac) % MOD
#         tem = (tem + fac * b % MOD) % MOD
#         flag = flag * fac % MOD
#         ans = ans * tem % MOD
#     ans = (ans + flag) % MOD
#     print(f"Case {t + 1}: {ans}")
# Accepted	PYTH3	0.130

# UVa 12546 - LCM Pair Sum
# MOD = 1000000007

# def main():
#     t = int(input())  # 讀取測試案例數量
#     for k in range(1, t + 1):  # 對每個測試案例進行迴圈
#         c = int(input())  # 讀取質因數數量
#         factors = [tuple(map(int, input().split())) for _ in range(c)]

#         n = 1
#         nums = []
#         for factor, power in factors:
#             prev = 1
#             num = 1
#             for _ in range(power):
#                 prev = (prev * factor) % MOD  # 計算每個質因數的冪
#                 num = (num + prev) % MOD  # 累加到 num
#                 print(prev, num)
#             num = (num + (power * prev) % MOD) % MOD  # 加上額外貢獻
#             nums.append(num)
#             print(nums)
#             n = (n * prev) % MOD  # 更新 n
#         print(n, 'a')
#         ans = 1
#         for num in nums:
#             ans = (ans * num) % MOD  # 計算最終答案
#         ans = (ans + n) % MOD

#         print(f"Case {k}: {ans}")

# if __name__ == "__main__":
#     main()
# Accepted	PYTH3	0.270

