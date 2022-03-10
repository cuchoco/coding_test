# 정수 x에 대해 x가 5로나누어디면 5로나눔
# 3이면 3, 2면2
# 아니면 1빼기. 1로 만드는 최솟값은?

x = 26 # 연산횟수는 3
count = 0


# 바텀업

def func(x):
    d = [0] * 1000

    for i in range(2, x+1):
        # 1을 빼는 경우
        d[i] = d[i-1] + 1

        if i % 2 == 0:
            d[i] = min(d[i], d[i//2] + 1)

        if i % 3 == 0:
            d[i] = min(d[i], d[i//3] + 1)

        if i % 5 == 0:
            d[i] = min(d[i], d[i//5] + 1)
    
    return d[x]



print('x:' ,x , 'count:',func(x))


        



