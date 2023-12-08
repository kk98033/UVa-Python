''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 11005 - Cheapest Base
def solve(table, nums):
    tableDict = {}
    index = 0
    for _ in range(36):
        tableDict[index] = table[index]
        index += 1

    for n in nums:
        costs = [0] * 37
        ans = []
        for base in range(2, 37):
            tempNum = n
            cost = 0
            while tempNum:
                cost += tableDict[tempNum % base]
                tempNum //= base
            costs[base] = cost

        minCost = min(costs[2:])
        for base, cost in enumerate(costs):
            if base == 0 or base == 1: continue
            if cost == minCost:
                ans.append(base)
        print(f'Cheapest base(s) for number { n }: { " ".join(map(str, ans)) }')

T = int(input())
for t in range(T):
    table = []
    for i in range(4):
        table.extend(list(map(int, input().split())))

    nums = []
    for i in range(int(input())):
        nums.append(int(input()))

    if t != 0: print()
    print(f'Case { t+1 }:')
    solve(table, nums)