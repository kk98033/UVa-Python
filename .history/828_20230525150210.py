''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# UVa 828 - Deciphering Messages
def solve(key, numKey, texts):
    def decrypt(char):
        # alphabetTable = {chr(i): i for i in range(ord('A'), ord('Z')+1)}
        # A: 65, Z: 90
        # print(char, (ord(char) - numKey), chr(ord(char) - numKey))
        if char == ' ': return char
        if ord(char) - numKey < 65:
            return chr(ord(char) - numKey + 26)
        return chr(ord(char) - numKey)
    for text in texts:
        index = cur = 0
        ans = ''
        # RTS SKA E AGE
        #  R   I  C  E
        error = False
        while index < len(text):
            if index + 2 < len(text) and (text[index] == key[cur%len(key)] and text[index+2] == key[(cur+1)%len(key)]):
                temp = decrypt(text[index+1])
                if temp in key:
                    ans += temp
                else:
                    error = True
                    break
                # ans += text[index+1]
                index += 3
                cur += 1
            else:
                temp = decrypt(text[index])
                if temp not in key:
                    ans += temp
                else:
                    error = True
                    break
                # ans += text[index]
                index += 1
            # except:
            #     break
        if error:
            print('error in encryption')
        else:
            print(ans)

    # return key, numKey, texts

T = int(input())
for t in range(T):
    input() # blank
    key = input()
    numKey = int(input())
    n = int(input())
    texts = []
    for i in range(n):
        texts.append(input())

    if t != 0: print()

    solve(key, numKey, texts)
# Accepted	PYTH3	0.040