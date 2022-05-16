
#### 재귀함수 방법 ####
nIteration = int(input())

def solution(n):
    if n == 0:
        return 2
    if n > 0:
        return (2*solution(n-1)-1) 

print(solution(nIteration)**2)

#### DP TABLE ####  < 이게 더 오래걸림.

dpTable = [-1] * 15
dpTable[0] = 2

for i in range(1, 15):
    dpTable[i] = 2 * dpTable[i-1] -1

print(dpTable[nIteration]**2)