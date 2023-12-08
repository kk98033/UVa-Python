''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def getPrimeTable():
    primeTable = [i for i in range(2, 100) if isPrime(i)]
    return primeTable

def solve(n):
    ansList = []
    curIndex = 0
    for i in range(n+1):
        for index, prime in enumerate(primeTable):
            if i == 0 or prime > i: break
            while i > 0 and i % prime == 0:
                if curIndex <= index:
                    ansList.append(0)
                    curIndex += 1
                ansList[index] += 1
                i //= prime

    head = f'{n:>3}! ='
    print(head, end='')
    for i, ans in enumerate(ansList):
        if (i + 1) % 15 == 0: 
            print()
            print(len(head) * ' ')
        print(' ', ans, end='')
    print()

primeTable = getPrimeTable()
while True:
    try:
        n = int(input())
        if n == 0: break

        solve(n)
    except EOFError:
        break