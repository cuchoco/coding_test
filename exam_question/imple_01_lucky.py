data1 = '123402'
data2 = '7755'

def solution(data):
    data = list(map(int, data))   
    n = len(data)
    pivot = (n // 2)
    
    if sum(data[:pivot]) == sum(data[pivot:]):
        return 'LUCKY'

    else:
        return 'READY'


print(solution(data1))
print(solution(data2))
