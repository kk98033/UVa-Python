''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 12019 - Doom's Day Algorithm
def solve(month, date):
    # Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
    # 1/6 - Thursday
    # 1/5 - Wednesday
    # 1/4 - Tuesday
    # 1/3 - Monday
    # 1/2 - Sunday
    # 1/1 - Saturday

    # 月份天數
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 星期名稱
    weekOfDay = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    # 從1月1日到給定日期的總天數
    days = date # 已經包括當月到目前日期的天數
    for i in range(month - 1): # 只累加到前一個月（）
        days += months[i]

    # 計算星期幾
    return weekOfDay[(days-1) % 7]
 
T = int(input())
for t in range(T):
    month, date = list(map(int, input().split()))
    print(solve(month, date))
# 	Accepted	PYTH3	0.050