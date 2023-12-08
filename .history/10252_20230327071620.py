''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10252 - Common Permutation
def solve(n1, n2):
    ans = []
    n1Dic, n2Dic = {}, {}
    for i in n1:
        n1Dic[i] = n1Dic.get(i, 0) + 1
    for i in n2:
        n2Dic[i] = n2Dic.get(i, 0) + 1

    for key, item in n1Dic.items():
        if key in n1 and key in n2:
            ans.extend([key] * min(n1Dic[key], n2Dic[key]))
    return ''.join(sorted(ans))

while True:
    try:
        n1 = input()
        n2 = input()

        print(solve(n1, n2))
    except EOFError:
        break