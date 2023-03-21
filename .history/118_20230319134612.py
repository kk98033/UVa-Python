''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

'''
   N
w -|- E
   S
'''

move = {
        'N': (0, 1),  # go up - N
        'S': (0, -1), # go down - S
        'E': (1, 0),  # go right - E
        'W': (-1, 0)  # go left - W
    }

falls = []

def turn(faces: str, direction: str) -> str:
    dirs = ['N', 'E', 'S', 'W']
    cur = dirs.index(faces)
    direction = 1 if direction == 'R' else -1
    if cur + direction < 0: return dirs[-1]
    if cur + direction > 3: return dirs[0]
    return dirs[cur + direction]

def solve(width, height, pos, faces, codes):
    # pos -> [x, y]
    for code in codes:
        # print(pos, faces, 'LOST', i, code)
        if code == 'F':
            if pos in falls:
                print('fall', pos)
                continue

            pos[0] += move[faces][0]
            pos[1] += move[faces][1]
            if (pos[0] < 0 or pos[0] > width) or (pos[1] < 0 or pos[1] > height):
                print(falls, pos)
                pos[0] -= move[faces][0]
                pos[1] -= move[faces][1]
                falls.append(pos) # save postiton
                return pos, faces, 'LOST'
        else:
            faces = turn(faces, code)


    return pos, faces

width, height = list(map(int, input().split()))
while True:
    try:
        x, y, faces = input().split()
        codes = input()

        print(solve(width, height, [int(x), int(y)], faces, codes))
    except EOFError:
        break