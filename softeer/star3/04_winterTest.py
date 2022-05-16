# 입력
# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 1 1 0 0 0 0
# 0 0 0 1 1 0 1 1 0
# 0 0 1 1 1 1 1 1 0
# 0 0 1 1 1 1 1 0 0
# 0 0 1 1 0 1 1 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0

# 출력
# 4
from functools import reduce

n, m = list(map(int, input().split()))
matrix = [[0]* m for _ in range(n)]

for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(m):
        matrix[i][j] = lst[j]

time = 0
fin = True
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            fin = False
            # 동 서 남 북
            # matrix[i][j+1] , matrix[i][j-1] , matrix[i+1][j] , matrix[i-1][j] 
            # 왼쪽 테두리인 경우 > 동 북 남 확인
            if j == 0:
                if matrix[i][j+1] + matrix[i+1][j] + matrix[i-1][j] <= 1:
                    matrix[i][j] == -1
                # 왼쪽 위 모서리 > 동 남 확인
                if i == 0:
                
                # 왼쪽 아래 모서리 > 북 동 확인
                if i == n-1:

        
   