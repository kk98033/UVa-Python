''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# -*- coding: UTF-8 -*-
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}


# UVa 11321 - Sort! Sort!! and Sort!!!
# https://stackoverflow.com/questions/5213033/sort-a-list-of-lists-with-a-custom-compare-function
from functools import cmp_to_key
def solve(n, m, nums):
    # 1. 先利用每個數字除以M的餘數由小到大排
    # 2. 若排序中比較的兩數為一奇一偶且兩數除以M的餘數相等，則奇數要排在偶數前面。
    # 3. 若兩奇數除以M餘數大小相等，則原本數值較大的奇數排在前面。
    # 4. 若兩偶數除以M餘數大小相等，則較小的偶數排在前面。
    def comapre(item1, item2):
        # return a negative value (< 0) when the left item should be sorted before the right item
        # return a positive value (> 0) when the left item should be sorted after the right item

        modulo1, modulo2 = abs(item1) % m, abs(item2) % m
        if item1 < 0 and m > 0: modulo1 = -modulo1
        if item2 < 0 and m > 0: modulo2 = -modulo2

        if modulo1 != modulo2: # rule 1
            if modulo1 > modulo2:
                return 1
            else:
                return -1
        
        else: # equal
            if item1 % 2 != item2 % 2: # rule 2
                if item1 % 2 == 1: # odd
                    return -1
                else: # even
                    return 1
            
            if item1 % 2 == 1 and item2 % 2 == 1: # odd
                return item2 - item1
            
            if item1 % 2 == 0 and item2 % 2 == 0: # even
                return item1 - item2

    ans = sorted(nums, key=cmp_to_key(comapre))
    return '\n'.join(map(str, ans))

while True:
    n, m = list(map(int, input().split()))
    print(f'{n} {m}')
    if n == 0 and m == 0: break
    nums = []
    for i in range(n):
        nums.append(int(input()))

    print(solve(n, m, nums))
# Accepted	PYTH3	2.610