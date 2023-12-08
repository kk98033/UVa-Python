''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def solve(month, date):
    # Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
    # 1/6 - Thursday
    # 1/5 - Wednesday
    # 1/4 - Tuesday
    # 1/3 - Monday
    # 1/2 - Sunday
    # 1/1 - Saturday
    months = {
        1: 31, 2: 28, 3: 31,
        4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30,
        10: 31, 11: 30, 12: 31
    }
    days = 0
    for i in range(1, month):
        days += months[i]
    days += date
    return days

T = int(input())
for t in range(T):
    month, date = list(map(int, input().split()))
    print(solve(month, date))