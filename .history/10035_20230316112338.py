''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(n1, n2):
    count = 0
    carry = 0
    index = 0
    while index < len(n1) and index < len(n2):
        # if n1[index] + n2[index] >= 10:
        #     count += 1
        carry = (int(n1[index]) + int(n2[index]) + carry) % 10
        if carry != 0: count += 1
        index += 1
    return 'No carry operation.' if count == 0 else f'{ count } carry operations.'

while True:
    try:
        n1, n2 = list(map(int, input().split()))
        if n1 == 0 and n2 == 0: break
        print(solve(str(n1)[::-1], str(n2)[::-1]))
    except EOFError:
        break