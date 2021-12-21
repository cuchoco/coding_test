# n: 배열의 크기 m: 숫자가 더해지는 횟수 k:연속 해서 k번을 초과해서 더해질수 없다.
def big_num(n:int=4, m:int=5, k:int=3, data:list=[3,4,5,6]) -> int:
    assert len(data) == n
    answer = 0
    data.sort(reverse=True)
    first = data[0]
    second = data[1]
    
    while m > 0:
        answer += first
        m -=1
        k -=1
        if k == 0:
            answer += second
            m -=1
            k = 3
    return answer

print(big_num(5,8,3, [2,4,5,4,6]))

        
