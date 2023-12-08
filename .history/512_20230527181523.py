''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(row, col, codeNum, operations, n, checks):
    def DR(rows):
        for i in sorted(rows)[::-1]:
            tempTable.pop(i-1)
        return
    
    def DC(c):
        for c in sorted(c)[::-1]:
            for row in tempTable:
                row.pop(c-1)
        return
    
    def IR(rows):
        for i in sorted(rows)[::-1]:
            tempTable.insert(i-1, [(0, 0)] * len(tempTable[0]))
        return
    
    def IC(c):
        for c in sorted(c)[::-1]:
            for row in tempTable:
                row.insert(c-1, (0, 0))
        return
    
    def EX(pos):
        
        r1, c1 = pos[0] - 1, pos[1] - 1
        r2, c2 = pos[2] - 1, pos[3] - 1
        tempTable[r1][c1], tempTable[r2][c2] = tempTable[r2][c2], tempTable[r1][c1]
        # print(tempTable[r1][c1], tempTable[r2][c2] )
        return
    
    tempTable = [[(i+1, j+1) for j in range(col)] for i in range(row)]
    # for i in table:
    #     print(i)
    

    for oper in operations:
        if oper[0] == 'DR':
            DR(oper[2:])
        elif oper[0] == 'DC':
            DC(oper[2:])
        elif oper[0] == 'IR':
            IR(oper[2:])
        elif oper[0] == 'IC':
            IC(oper[2:])
        elif oper[0] == 'EX':
            EX(oper[1:])

        # print('-----')
        # print(oper[0])
        # for i in tempTable:
        #     print(i)
        # print()

    for pos in checks:
        found = False
        for i in range(len(tempTable)):
            for j in range(len(tempTable[0])):
                if (pos[0], pos[1]) == tempTable[i][j]:
                    print(f'Cell data in ({ pos[0] },{ pos[1] }) moved to ({ i+1 },{ j+1 })')
                    found = True
                    break
            if found: break
        if not found:
            print(f'Cell data in ({ pos[0] },{ pos[1] }) GONE')
        

        # print(pos)

    # print()
    # for i in tempTable:
    #     print(i)


t = 1
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

        if t != 1: print()
        print(f'Spreadsheet #{t}')
        solve(row, col, codeNum, operations, n, checks)
        t += 1
        input() # blank
    except EOFError:
        break