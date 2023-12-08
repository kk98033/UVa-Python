''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10908 - Largest Square
def check(m, n, row, col):
    print('--------------------')
    mid = matrix[row][col]
    # topLeftRow, topLeftCol = row - length, col - length
    prevLen = 1
    length = 3
    index = 1
    while True:
        topLeftRow, topLeftCol = row - (index), col - (index)
        curRow, curCol = topLeftRow, topLeftCol
        print()
        print(curRow, curCol, mid, length)

        for i in range(length-1): # top row (left -> right)
            curCol += 1
            # print(length, prevLen)
            # print(matrix[curRow][curCol], curRow, curCol)
            if 0 <= curCol < n and matrix[curRow][curCol] == mid: 
                print(curRow, curCol, length, matrix[curRow][curCol], 'aaaaaaa')
                continue
            else: 
                return prevLen

        for i in range(length-1): # right column (top -> bottom)
            curRow += 1
            # print(curRow, curCol, length)
            if 0 <= curRow < m and matrix[curRow][curCol] == mid: 
                print(curRow, curCol, length, matrix[curRow][curCol])
                continue
            else: 
                return prevLen

        for i in range(length-1): # bottom row (right -> left)
            curCol -= 1
            # print(curRow, curCol, length)
            if 0 <= curCol < n and matrix[curRow][curCol] == mid: 
                print(curRow, curCol, length, matrix[curRow][curCol])
                continue
            else: 
                return prevLen

        for i in range(length-1): # left column (bottom -> top)
            curRow -= 1
            # print(curRow, curCol, length)
            if 0 <= curRow < m and matrix[curRow][curCol] == mid: 
                print(curRow, curCol, length, matrix[curRow][curCol])
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
        print(check(m, n, row, col), '=====')    