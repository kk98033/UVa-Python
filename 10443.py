''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10443 - Rock, Scissors, Paper
def solve2(row, col, turn, field):
    dirs = [
        (1, 0), (-1, 0), (0, 1), (0, -1)
    ]
    for _ in range(turn):
        update = set()
        for r in range(row):
            for c in range(col):
                cur = field[r][c]
                for x, y in dirs:
                    if 0 <= r + x < row and 0 <= c + y < col:
                        opponent = field[r+x][c+y]
                        if (cur, opponent) in [('R', 'S'), ('P', 'R'), ('S', 'P')]:
                            update.add((cur, r+x, c+y))

        for state, r2, c2 in update:
            field[r2][c2] = state

    return field

import sys
def solve(row, col, turn, field):
    dirs = [
        (1, 0), (-1, 0), (0, 1), (0, -1)
    ]
    for _ in range(turn):
        update = set()
        for r in range(row):
            for c in range(col):
                cur = field[r][c]
                for x, y in dirs:
                    if 0 <= r + x < row and 0 <= c + y < col:
                        opponent = field[r+x][c+y]
                        if (opponent, cur) in [('R', 'S'), ('P', 'R'), ('S', 'P')]:
                            update.add((opponent, r, c))
                            break

        for state, r2, c2 in update:
            field[r2][c2] = state

    return field

# while True:
#     try:
#         T = int(input())
#         for t in range(T):
#             row, col, turn = list(map(int, input().split()))
#             field = [list(sys.stdin.readline().strip()) for _ in range(row)]

#             if t != 0:
#                 print()
#             ans = solve(row, col, turn, field)
#             for r in ans:
#                 print(''.join(r))

#     except EOFError:
#         break
# UVa online judge: Time limit exceeded	PYTH3	3.000

# CPE 解答轉 Python:
# UVa online judge 依然 TLE :(
# def solve(r, c, n, board):
#     for d in range(n):
#         today = d % 2
#         tomorrow = (d + 1) % 2

#         for i in range(1, r + 1):
#             for j in range(1, c + 1):
#                 if board[today][i][j] == 'R':
#                     win = 'P'
#                 elif board[today][i][j] == 'P':
#                     win = 'S'
#                 else:
#                     win = 'R'

#                 if (board[today][i + 1][j] == win or board[today][i][j + 1] == win or
#                     board[today][i - 1][j] == win or board[today][i][j - 1] == win):
#                     board[tomorrow][i][j] = win
#                 else:
#                     board[tomorrow][i][j] = board[today][i][j]

#     return board[tomorrow]

# def main():
#     T = int(input())
#     for _ in range(T):
#         r, c, n = map(int, input().split())
#         board = [[['X'] * (c + 2) for _ in range(r + 2)] for _ in range(2)]

#         for i in range(1, r + 1):
#             row = input()
#             for j in range(1, c + 1):
#                 board[0][i][j] = row[j - 1]

#         result = solve(r, c, n, board)
#         for i in range(1, r + 1):
#             print(''.join(result[i][1:c + 1]))
#         if _ < T - 1:
#             print()

# if __name__ == "__main__":
#     main()
# UVa online judge: Time limit exceeded	PYTH3	3.000