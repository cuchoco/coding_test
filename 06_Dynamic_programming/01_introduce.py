# 동적 계획법에 대한 설명
# 다이나믹 프로그래밍의 2가지 방식(TopDown, BottomUp)
# 메모이제이션 기법
# 프로그래밍에서 다이나믹은 '프로그램이 실행되는 도중에' 라는 의미
# 자료구조에서의 동적 할당은 프로그램 실행중에 프로그램 실행에 필요한 메모리를 할당하는 기법.

# ex) 피보나치 수열
# 수열을 배열이나 리스트로 표현할 수 있다.


# 점화식이나 재귀함수를 사용해 만들 수는 있지만, 효율적이지않음(x 가 50만 되어도 엄청난 시간이 걸림)

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print('recursively implement:\t',fibo(28))


# 다이나믹 프로그래밍의 조건
# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포합하는 큰 문제에서도 동일하다.

# 메모이제이션 기법: 한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 그대로 가져옴
# 캐싱(Caching) 이라고도 한다.

# 재귀적으로 구현한 피보나치 수열(TopDown)

d = [0] * 100

def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print('memoization recursively:\t', fibo(28))

# 반복적으로 구현한 피보나치 수열(BottomUP) 여기서 d는 DP 테이블이라고 부름 (메모이제이션과 다름)

d = [0] * 100

def fibo(x):
    d[1] = 1
    d[2] = 1
    
    for i in range(3, x+1):
        d[i] = d[i-1] + d[i-2]

    return d[x]

print('memoization repeat:\t', fibo(28))