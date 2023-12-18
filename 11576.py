''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# 11576 - Scrolling Sign
def solve(k, w, signs):
    ans = k
    for i in range(w-1):
        sameLetters = k
        for sameLetters in range(k, -1, -1):
            if signs[i][k-sameLetters:] == signs[i+1][0:sameLetters]:
                break
        ans += k - sameLetters
    return ans

T = int(input())
for t in range(T):
    k, w = list(map(int, input().split()))
    signs = [[i for i in input()] for _ in range(w)]
    print(solve(k, w, signs))
# 	Accepted	PYTH3	0.040