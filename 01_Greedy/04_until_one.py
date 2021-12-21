# 1.N에서 1을 뺀다. 
# 2.N을 K로 나눈다.

def make_one(N:int, K:int) -> int:
    count = 0
    while N != 1:
        if N % K ==0 and N / K >= 1:
            N /= K
            count +=1
        else:
            N -= 1
            count +=1
    return count

print(make_one(95000, 132))
