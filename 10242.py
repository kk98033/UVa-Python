''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 10242 - Fourth Point !!
def solve(x1, y1, x2, y2, x3, y3, x4, y4):
    if x1 == x3 and y1 == y3: # 檢查點1和點3是否相同（即它們是平行四邊形的中點）
        return f"{(x2 + x4) - x1:.3f} {(y2 + y4) - y1:.3f}"
    
    elif x1 == x4 and y1 == y4: # 檢查點1和點4是否相同
        return f"{(x2 + x3) - x1:.3f} {(y2 + y3) - y1:.3f}"
    
    elif x2 == x3 and y2 == y3: # 檢查點2和點3是否相同
        return f"{(x1 + x4) - x2:.3f} {(y1 + y4) - y2:.3f}"
    
    else: # 如果上述條件都不符合，則點2和點4是中點
        return f"{(x1 + x3) - x2:.3f} {(y1 + y3) - y2:.3f}"

while True:
    try:
        points = list(map(float, input().split()))
        print(solve(*points))
    except EOFError:
        break
# ???