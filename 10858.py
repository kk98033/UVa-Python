''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10858 - Unique Factorization
def dfs(result, cur_list, factors, target):
    # print(result, cur_list, factors, target)
    if result == target:
        ans.append(cur_list)
        return
    
    if result > target:
        return
    
    for i in range(len(factors)):
        dfs(result*factors[i], cur_list + [factors[i]], factors[i:], target)

    return

def dfs2(result, cur_list, factors, target, start):
    if result == target:
        ans.append(cur_list)
        return
    
    for i in range(start, len(factors)):
        if result * factors[i] > target:
            break
        dfs2(result * factors[i], cur_list + [factors[i]], factors, target, i)


while True:
    try:
        ans = []
        n = int(input())
        if n == 1: 
            print(0)
            continue
        if n == 0: break

        factors = []
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if i != n // i:
                    factors.append(i)
                    factors.append(n // i)
                else: 
                    factors.append(i)
        factors.sort()
        # print(factors)
        # dfs(1, [], factors, n)
        dfs2(1, [], factors, n, 0)
        print(len(ans))
        for i in ans:
            print(' '.join([str(j) for j in i]))
    except EOFError:
        break
# dfs1: 	Accepted	PYTH3	0.120
# dfs2:	    Accepted	PYTH3	0.050