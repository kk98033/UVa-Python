''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(row, col, codeNum, operations, n, checks):
    def DR(r):
        return
    def DC(c):
        return
    def IR(r):
        return
    def IC(c):
        return
    def EX(r, c):
        return
    
    table = [[(i, j) for j in range(col)] for i in range(row)]
    for i in table:
        print(i)

    return operations

while True:
    try:
        row, col = list(map(int, input().split()))
        if (row, col) == (0, 0): break
        codeNum = int(input())
        operations = []
        for i in range(codeNum):
            temp = input().split()
            operations.append([temp[0]] + list(map(int, temp[1:])))

        n = int(input())
        checks = []
        for i in range(n):
            checks.append(list(map(int, input().split())))

        print(solve(row, col, codeNum, operations, n, checks))
    except EOFError:
        break