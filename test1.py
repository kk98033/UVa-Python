''' 1 '''

def plusMult(A):
    # Write your code here
    # print(A)
    even = odd = 0
    eCount = oCount = 0
    for i in range(len(A)):
        if i % 2 == 0:
            if eCount % 2 == 0:
                even += A[i]
            else:
                even *= A[i]
            eCount += 1
        else:
            if oCount % 2 == 0:
                odd += A[i]
            else:
                odd *= A[i]
            oCount += 1
    even = even % 2
    odd = odd % 2
    if odd > even:
        return 'ODD'
    if even > odd:
        return 'EVEN'
    return 'NEUTRAL'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    A_count = int(input().strip())

    A = []

    for _ in range(A_count):
        A_item = int(input().strip())
        A.append(A_item)

    result = plusMult(A)

    fptr.write(result + '\n')

    fptr.close()

'''
10
1
2
3
4
5
6
7
8
9
10

EVEN
'''