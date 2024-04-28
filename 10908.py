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
    length = 1
    index = 1
    while True:
        newLength = length + 2
        topLeftRow, topLeftCol = row - index, col - index # 新的正方形左上角座標

        # 檢查邊界
        if not (0 <= topLeftRow < m and 0 <= topLeftCol < n and 
                topLeftRow + newLength - 1 < m and topLeftCol + newLength - 1 < n):
            return length
        
        # 檢查邊框上的所有字符是否與中心點字符相同
        for i in range(newLength):
            # 檢查上下邊框和左右邊框            
            if not (matrix[topLeftRow][topLeftCol + i] == mid and
                    matrix[topLeftRow + newLength - 1][topLeftCol + i] == mid and
                    matrix[topLeftRow + i][topLeftCol] == mid and
                    matrix[topLeftRow + i][topLeftCol + newLength - 1] == mid):
                return length

        length = newLength
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
# Accepted	PYTH3	0.050