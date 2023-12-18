''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# 442 - Matrix Chain Multiplication
def solve(n, matrix, exp):
    stack = []
    ans = 0
    for i in exp:
        if i != ')':
            stack.append(i)
        else:
            tempMatrix = []
            while stack and stack[-1] != '(':
                tempMatrix.append(stack.pop())
            stack.pop()

            m1x, m1y = matrix[tempMatrix[1]]
            m2x, m2y = matrix[tempMatrix[0]]
            if m1y == m2x:
                ans += m1x * m1y * m2y
            else:
                return 'error'
            
            matrix[f'{ tempMatrix[1] }{ tempMatrix[0] }'] = m1x, m2y
            stack.append(f'{ tempMatrix[1] }{ tempMatrix[0] }')

    return ans

n = int(input())
matrix = {}
for _ in range(n):
    m, x, y = input().split()
    matrix[m] = (int(x), int(y))
    expressions = []
while True:
    try:
        # expressions.append(list(input()))
        print(solve(n, matrix, list(input())))
    except EOFError:
        break
# Accepted	PYTH3	0.010