''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(m, n, q, matrix, centers):
    def check(row, col):
        length = 1
        mid = matrix[row][col]
        topLeftRow, topLeftCol = row - length, col - length
        while True:
            curRow, curCol = topLeftRow, topLeftCol

            print(topLeftRow, topLeftCol, (row, col))

            for i in range(length): # top row (left -> right)
                curCol += i
                if 0 <= curCol < n and matrix[curRow][curCol] == mid: continue
                else: return length

            for i in range(length): # right column (top -> bottom)
                curRow += i
                if 0 <= curRow < n and matrix[curRow][curCol] == mid: continue
                else: return length

            for i in range(length): # bottom row (right -> left)
                curCol -= i
                if 0 <= curCol < n and matrix[curRow][curCol] == mid: continue
                else: return length

            for i in range(length): # left column (bottom -> top)
                curRow -= i
                if 0 <= curRow < n and matrix[curRow][curCol] == mid: continue
                else: return length

            length += 2
            topLeftRow, topLeftCol = row - length - 1, col - length - 1

    for row, col in centers:
        print(check(row, col))

    print(centers)
    return matrix

T = int(input())
for t in range(T):
    m, n, q = list(map(int, input().split()))
    matrix = []
    for i in range(m):
        matrix.append(list(input()))

    centers = []
    for i in range(q):
        centers.append(list(map(int, input().split())))

    print(solve(m, n, q, matrix, centers))