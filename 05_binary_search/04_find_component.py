# N개의 부품 정수 형태의 고유 번호존재 
# 손님이 M개의 부품 대량구매, 가게안에 부품이 모두 있는지 확인

from array import array
from unittest import result


N = 5
component = [8,3,7,9,2]

M = 3 
target = [5,7,9]



def findComp(component, target):
    answer = []

    for i in target:
        if i in component:
            answer.append('yes')
        else:
            answer.append('no')

    return answer


print("My answer:\t",findComp(component, target))


# ------------------------
# binary search

def binary_search(component, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if component[mid] == target:
            return mid
        elif component[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

component.sort()
answer = []

for i in target:
    result = binary_search(component,i, 0, N-1)

    if result != None:
        answer.append('yes')
    else:
        answer.append('no')

print("binary_search:\t", answer)
