''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}


def solve(key, numKey, texts):
    for text in texts:
        index = cur = 0
        ans = ''
        while index < len(text):
            if text[index] == key[cur] and text[index] == key[cur+2]:
                ans += text[index+1]
                index += 2
                cur += 1
            index += 1
        print(ans)

    return key, numKey, texts

T = int(input())
for t in range(T):
    input() # blank
    key = input()
    numKey = int(input())
    n = int(input())
    texts = []
    for i in range(n):
        texts.append(input())

    print(solve(key, numKey, texts))