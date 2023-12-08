''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 12015 - Google is Feeling Lucky
def solve(urls):
    urls.sort(key=lambda x: int(x[1]), reverse=True)
    for url, times in urls:
        if times == urls[0][1]:
            print(url)
        else: break

T = int(input())
for t in range(T):
    urls = []
    for i in range(10):
        urls.append(input().split())

    print(f'Case #{t+1}')
    solve(urls)