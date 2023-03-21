''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

from collections import Counter
def solve(text):
    ans = {}
    for i in text:
        if 'A' <= i <= 'Z':
            ans[i] = ans.get(i, 0) + 1
    ansList = [f'{key} {val}' for key, val in ans.items()]
    ansList.sort(key=lambda x: (-int(x[2]), x[0]))
    return '\n'.join(ansList)

def solveOneLine(text):
    return '\n'.join(sorted([f'{key} {val}' for key, val in Counter([i for i in text if 'A' <= i <= 'Z']).items()], key=lambda x: (-int(x[2]), x[0])))


T = int(input())
text = ''
for t in range(T):
    text += input()
# print(solve(text.upper()))
print(solveOneLine(text.upper()))
# Accepted	PYTH3	0.000