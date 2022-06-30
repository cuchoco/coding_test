# https://programmers.co.kr/learn/courses/30/lessons/92335

def conversion(n, k):
    res = ''
    while n:
        res += str(n % k)
        n //= k
    return res[::-1]
    

def prime_number(x):
    if x == 1:
        return False
    
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            answer += 1

    return True if answer == 1 else False


def solution(n, k):
    answer = 0
    res = conversion(n, k)
    res = res.split('0')
    for i in res:
        if i:
            if prime_number(int(i)):
                answer += 1
    return answer