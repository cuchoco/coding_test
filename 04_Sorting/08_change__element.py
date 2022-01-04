# 두 배열의 원소교체

def chg_ele(A, B, K): # to maximize A 
    A.sort()
    B.sort(reverse=True)
    
    for i in range(K):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
        else:
            break

    return sum(A)

A = [1,2,5,4,3]
B = [5,5,6,6,5]

print(chg_ele(A, B, 3))