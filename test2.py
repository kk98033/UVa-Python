''' 2 '''
import heapq
def minimumTime(ability, processes):
    # Write your code here
    
    maxHeap = [-i for i in ability]
    heapq.heapify(maxHeap)
    time = 0
    
    while processes > 0:
        maxAbility = -heapq.heappop(maxHeap)
        processes -= maxAbility
        time += 1
        
        nextAbility = maxAbility // 2
        heapq.heappush(maxHeap, -nextAbility)
    return time
    # TLE
    # time = 0
    # ability.sort(reverse=True)
    # while processes > 0:
    #     processes -= ability[0]
    #     time += 1
    #     ability[0] = ability[0] // 2
    #     ability.sort(reverse=True)
    # return time
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ability_count = int(input().strip())

    ability = []

    for _ in range(ability_count):
        ability_item = int(input().strip())
        ability.append(ability_item)

    processes = int(input().strip())

    result = minimumTime(ability, processes)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
5
2
1
5
3
1
17

9
'''