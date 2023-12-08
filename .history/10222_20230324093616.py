''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}

# Thanks for you dictionary bro :D https://zerojudge.tw/ShowThread?postid=33728&reply=0
def solve(s):
    return ''.join([dict[i] for i in s])

# 反斜線要用: '\\'表示
dict = {
        'e':'q','d':'a','c':'z','r':'w','f':'s','v':'x','t':'e','g':'d','b':'c','y':'r','h':'f','n':'v','u':'t','j':'g','m':'b','i':'y','k':'h',',':'n','o':'u',
        'l':'j','.':'m','p':'i',';':'k','/':',','[':'o',"'":'l',']':'p','2':'`','3':'1','4':'2','5':'3','6':'4','7':'5','8':'6','9':'7','0':'8','-':'9','=':'0', '\\': '' 
    } 

while True:
    try:
        s = input()
        print(solve(s))
    except EOFError:
        break