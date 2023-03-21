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
        carry = 1 if (int(n1[index]) + int(n2[index]) + carry) >= 10 else 0
        count += carry
        index += 1

    while index < len(n1):
        carry = 1 if int(n1[index]) + carry >= 10 else 0
        count += carry
        index += 1
    while index < len(n2):
        carry = 1 if int(n2[index]) + carry >= 10 else 0
        count += carry
        index += 1

    end = 's' if count > 1 else ''
    return 'No carry operation.' if count == 0 else f'{ count } carry operation{ end }.'

def solve2(n1, n2):
    count = carry = 0
    while n1 > 0 and n2 > 0:
        carry = 1 if n1 % 10 + n2 % 10 + carry >= 10 else 0
        count += carry
        n1 = n1 // 10
        n2 = n2 // 10
    
    while n1 != 0:
        carry = 1 if n1 % 10 + carry >= 10 else 0
        count += carry
        n1 //= 10

    while n2 != 0:
        carry = 1 if n2 % 10 + carry >= 10 else 0
        count += carry
        n2 //= 10

    end = 's' if count > 1 else ''
    return 'No carry operation.' if count == 0 else f'{ count } carry operation{ end }.'

while True:
    try:
        n1, n2 = list(map(int, input().split()))
        if n1 == 0 and n2 == 0: break
        # print(solve(str(n1)[::-1], str(n2)[::-1]))
        print(solve2(n1, n2))
    except EOFError:
        break