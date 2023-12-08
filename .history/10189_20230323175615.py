''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(row, col, field):
    checks = [
        # (row, col)
        (-1, -1), # upper left
        (-1, 0), # up
        (-1, 1), # upper right

        (0, -1), # left
        (0, 1), # right

        (1, -1), # down left
        (1, 0), # down
        (1, 1), # down right 
    ]

    ans = [[0 for c in range(col)] for r in range(row)]

    for r in range(row):
        for c in range(col):
            if field[r][c] == '*':
                ans[r][c] = '*'
                continue

            count = 0
            for check in checks:
                if 0 <= r + check[0] < row and 0 <= c + check[1] < col:
                    if field[r+check[0]][c+check[1]] == '*':
                        count += 1
            ans[r][c] = str(count)

    return '\n'.join([''.join(i) for i in ans])

while True:
    try:
        row, col = list(map(int, input().split()))

        if row == 0 and col == 0: break

        field = []
        for i in range(row):
            field.append(list(input()))
        print(solve(row, col, field))
    except EOFError:
        break