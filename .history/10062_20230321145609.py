''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(s):
    dic = {}
    for i in s:
        dic[i] = dic.get(i, 0) + 1
    ans = sorted([[ord(key), val] for key, val in dic.items()], key=lambda x: (int(x[1]), -x[0]))
    return '\n'.join([f'{key} {val}'for key, val in ans])

count = 0
while True:
    try:
        s = input()
        if count != 0: print()
        # print(s)
        if s:
            print(solve(s))
        count += 1
    except EOFError:
        break