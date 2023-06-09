''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10093 - An Easy Problem!
def generate():
    num = {}
    index = 0
    for i in range(ord('0'), ord('9')+1):
        num[chr(i)] = index
        index += 1

    for i in range(ord('A'), ord('Z')+1):
        num[chr(i)] = index
        index += 1

    for i in range(ord('a'), ord('z')+1):
        num[chr(i)] = index
        index += 1
    return num

def solve(s):
    maxNum = max([num[i] for i in s if i in num])    
    sumS = sum([num[i] for i in s if i in num])    
    if maxNum == 0: return 2

    while maxNum <= 62:
        if sumS % maxNum == 0: 
            return maxNum + 1
        maxNum += 1
    return 'such number is impossible!'

num = generate()
while True:
    try:
        s = input().replace(' ', '')
        print(solve(s))
    except EOFError:
        break
# Accepted	PYTH3	0.160