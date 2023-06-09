''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 490 - Rotating Sentences
def solve(text):
    row, col = len(text), max([len(s) for s in text])
    ans = ''
    for i in range(col):
        temp = ''
        for j in range(row-1, -1, -1):
            if i >= len(text[j]):
                temp += ' '
            else:
                temp += text[j][i]
        ans += temp + '\n'
    return ans[:-1]

text = []
while True:
    try:
        text.append(list(input()))

    except EOFError:
        print(solve(text))
        break
# Accepted	PYTH3	0.010