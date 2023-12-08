''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# 10226 - Hardwood Species
from collections import Counter
def solve(trees):
    if t != 0: print()

    count = {}
    for tree in trees:
        count[tree] = count.get(tree, 0) + 1
    n = len(trees)

    ''' attempt 2 TLE '''
    ans = sorted(count.keys())
    ans = [f'{key} {count[key] / n * 100:.4f}' for key in ans]
    return '\n'.join(ans)

    ''' attempt 1 TLE '''
    ans = sorted([[tree, f'{round(amount / n * 100, 4):.4f}'] for tree, amount in count.items()], key=lambda x: x[0])
    return '\n'.join([f'{tree} {amount}' for tree, amount in ans])

def solve2(trees):
    count = Counter(trees)
    n = len(trees)
    ans = sorted(count.keys())
    ans = [f'{key} {count[key] / n * 100:.4f}' for key in ans]
    return '\n'.join(ans)

T = int(input())
for t in range(T):
    trees = []
    if t == 0: input()
    while True:
        try:
            tree = input()
            if tree: 
                trees.append(tree)
            else: 
                print(solve(trees))
                break
        except EOFError:
            # print(solve(trees))
            print(solve2(trees))
            break
# OnlineJudge: Time limit exceeded	PYTH3	3.000
# ZeroJudge: AC (5.2s, 76.1MB)