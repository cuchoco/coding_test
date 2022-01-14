# 순차탐색이란 리스트 안에 있는 특정한 데이터를 찾기 위해 
# 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

def sequential_search(n, target, array):

    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환

n = 5
target = 'jihwan'
array = ['hanul','jonggu','jihwan','taeil','sangwook ']

print(sequential_search(n, target, array))