''' Don't copy this '''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
''''''

def decipher_message(alphabetical_key, numerical_key, message):
    decrypted_message = ""
    m = 1
    l = len(alphabetical_key)

    for letter in message:
        if letter in alphabetical_key:
            index = alphabetical_key.index(letter)
            c = chr((index + numerical_key) % l + ord('A'))
            decrypted_message += alphabetical_key[(index + m) % l] + c + alphabetical_key[(index + m + 1) % l]
            m += 1
        elif letter == ' ':
            decrypted_message += ' '
            m = 1
        else:
            return "error in encryption"

    return decrypted_message

T = int(input())

for _ in range(T):
    input()  # Ignore the blank line
    alphabetical_key = input().strip()
    numerical_key = int(input())
    num_messages = int(input())

    for _ in range(num_messages):
        message = input().strip()
        decrypted = decipher_message(alphabetical_key, numerical_key, message)
        print(decrypted)

    if _ < T - 1:
        print()
