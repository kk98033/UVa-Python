''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10908 - Largest Square
def check(m, n, row, col):
    mid = matrix[row][col]
    prevLen = 1
    length = 3
    index = 1
    while True:
        topLeftRow, topLeftCol = row - (index), col - (index)
        curRow, curCol = topLeftRow, topLeftCol

        for i in range(length-1): # top row (left -> right)
            curCol += 1
            if 0 <= curCol < n and matrix[curRow][curCol] == mid: 
                continue
            else: 
                return prevLen

        for i in range(length-1): # right column (top -> bottom)
            curRow += 1
            if 0 <= curRow < m and matrix[curRow][curCol] == mid: 
                continue
            else: 
                return prevLen

        for i in range(length-1): # bottom row (right -> left)
            curCol -= 1
            if 0 <= curCol < n and matrix[curRow][curCol] == mid: 
                continue
            else: 
                return prevLen

        for i in range(length-1): # left column (bottom -> top)
            curRow -= 1
            if 0 <= curRow < m and matrix[curRow][curCol] == mid: 
                continue
            else: 
                return prevLen

        prevLen = length
        length += 2
        index += 1
        
T = int(input())
for t in range(T):
    m, n, q = list(map(int, input().split()))
    matrix = []
    for i in range(m):
        matrix.append(list(input()))

    centers = []
    for i in range(q):
        centers.append(list(map(int, input().split())))

    print(f'{ m } { n } { q }')
    for row, col in centers:
        print(check(m, n, row, col))    
# Accepted	PYTH3	0.140