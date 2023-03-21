''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10050 - Hartals
def solve(days, party):
    strike = set()
    for i in party:
        temp = i
        while temp <= days:
            if temp % 7 != 6 and temp % 7 != 0:
                strike.add(temp)
            temp += i

    return len(strike)

T = int(input())
for t in range(T):
    days = int(input())
    party = []
    for i in range(int(input())):
        party.append(int(input()))

    print(solve(days, party))
# Accepted	PYTH3	0.010