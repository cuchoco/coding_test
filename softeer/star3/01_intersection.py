# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=803

# 입력 예제
# 2
# 10 A
# 10 B
# 출력 예제
# 10
# 11

N = int(input())
A = []
B = []
C = []
D = []

for i in range(N):
    time, loc = list(input().split())
    eval(loc).append((i, int(time)))

    if i == 0:
        min_t = int(time)
    if i == N-1:
        max_t = int(time)

now = min_t
answer = [-1] * (N)


while ( A or B or C or D ):
    a_min = 1e9
    b_min = 1e9
    c_min = 1e9
    d_min = 1e9

    if A:
        a_min = A[0][1]
    if B:
        b_min = B[0][1]
    if C:
        c_min = C[0][1]
    if D:
        d_min = D[0][1]

    if ((a_min < now) or (b_min < now) or (c_min < now) or (d_min < now)):
        pass
    else:
        now = min([a_min, b_min, c_min, d_min]) 

    A_possible = False
    B_possible = False
    C_possible = False
    D_possible = False

    A_stuck = False
    B_stuck = False
    C_stuck = False
    D_stuck = False 

    if A:
        if (not D and A[0][1] <= now):
            A_possible = True

        if (D and  D[0][1] > now and A[0][1] <= now):
            A_possible = True

        if (A_possible and A[0][1] <= now):
            A_stuck = True

    if D:
        if (not C and D[0][1] <= now):
            D_possible = True

        if (C and  C[0][1] > now and D[0][1] <= now):
            D_possible = True

        if (D_possible and D[0][1] <= now):
            D_stuck = True

    if C:
        if (not B and C[0][1] <= now):
            C_possible = True

        if (B and  B[0][1] > now and C[0][1] <= now):
            C_possible = True

        if (C_possible and C[0][1] <= now):
            C_stuck = True


    if B:
        if (not A and B[0][1] <= now):
            B_possible = True

        if (A and  A[0][1] > now and B[0][1] <= now):
            B_possible = True

        if (B_possible and B[0][1] <= now):
            B_stuck = True 
        


    if (A_stuck and B_stuck and C_stuck and D_stuck):
        break

    if A_possible:
        answer[A[0][0]] = now
        A.pop(0)

    if B_possible:
        answer[B[0][0]] = now
        B.pop(0)

    if C_possible:
        answer[C[0][0]] = now
        C.pop(0)

    if D_possible:
        answer[D[0][0]] = now
        D.pop(0)

    now += 1


for i in range(len(answer)):
    print(answer[i])


    