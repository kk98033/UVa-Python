''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

from collections import defaultdict

alphabet = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4', 'e' : '5', 'f' : '6', 'g' : '7', 'h' : '8', 'i' : '9', 'j' : '10', 'k' : '11', 'l' : '12', 'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 'y' : '25', 'z' : '26'}


def decipher_message(alphabetical_key, numerical_key, message):
    decrypted_message = ""
    m = 1
    l = len(alphabetical_key)

    for letter in message:
        if letter in alphabetical_key:
            index = (alphabetical_key.index(letter) - m + l) % l
            c = chr((index + numerical_key) % l + ord('A'))
            decrypted_message += alphabetical_key[index] + c + alphabetical_key[(index + 1) % l]
            m += 1
        elif letter == ' ':
            decrypted_message += ' '
            m = 1
        else:
            return "error in encryption"

    return decrypted_message


# 读取输入的测试案例数量
num_cases = int(input())

# 处理每个测试案例
for _ in range(num_cases):
    input()  # 空行
    alphabetical_key = input().strip()
    numerical_key = int(input())
    num_messages = int(input())

    # 处理每个密文消息
    for _ in range(num_messages):
        encrypted_message = input().strip()
        decrypted_message = decipher_message(alphabetical_key, numerical_key, encrypted_message)
        print(decrypted_message)

    if _ < num_cases - 1:
        print()  # 输出空行分隔每个测试案例的结果
