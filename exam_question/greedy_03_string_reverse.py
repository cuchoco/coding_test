# 숫자를 모두 같게 만들어야하고 연속된 하나 이상의 숫자를 뒤집을수있다.
# ex) 0001100 은 4,5 번을 한번만 뒤집으면 다 같아짐.
# 최소횟수 구하는 프로그램.

data = '0001100'

def solution(data):
    zero = 0
    one = 0
    # 모두 1을 만드는 경우
    a = data.split('1')
    for i in a:
        if i:
            one +=1

    # 모두 0을 만드는 경우
    a = data.split('0')
    for i in a:
        if i:
            zero +=1

    return min(zero, one)

print(solution(data))