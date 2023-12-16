''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 12428 - Enemy at the Gates
# https://zh.wikipedia.org/zh-tw/%E5%AE%8C%E5%85%A8%E5%9C%96
def sovle(cities, roads):
    if cities > roads:
        return roads
    
    for i in range(cities - 1, -1, -1):
        connectedCities = cities - i
        leftRoad = roads - i
        if connectedCities * (connectedCities - 1) // 2 >= leftRoad:
            return i
T = int(input())
for t in range(T):
    cities, roads = list(map(int, input().split()))
    print(sovle(cities, roads))
# Accepted	PYTH3	0.070