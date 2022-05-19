K, P, N = list(map(int, input().split()))

def function(P, N):
    if N == 1:
        return P
    elif N % 2 == 0:   # 짝수인 경우
        a = function(P, N/2)
        return a*a % 1000000007
    else:            # 홀수인 경우
        b = function(P, (N-1)/2)
        return b*b*P % 1000000007

answer = (K*function(P, 10*N)) % 1000000007

print(answer)
