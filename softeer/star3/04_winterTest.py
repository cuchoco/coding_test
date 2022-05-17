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
from collections import deque

n, m = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(n)]

# 좌우 상하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]      
time = 0

def bfs():
    queue = deque([[0,0]])   # 얼음이 존재하지 않는 가장자리 지점 부터 시작
    visited[0][0] = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4): # 현재위치에서 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < n and 0 <= nx < m:
                if matrix[ny][nx]:   # 탐색하는 곳이 얼음이라면
                    visited[ny][nx] += 1 # 방문횟수 1 증가

                elif visited[ny][nx] == 0: # 탐색하는 곳이 얼음이 아니라면                    
                    queue.append([ny, nx])  # 그 지점도 탐색을 해야하므로 queue 삽입
                    visited[ny][nx] = 1 # 방문횟수 1로 초기화

    for y in range(n):
        for x in range(m):
            if visited[y][x] >= 2:
                matrix[y][x] = 0
            
while True:
    if matrix.count([0]*m) == n:
        break
    visited = [[0]*m for _ in range(n)]
    bfs()
    time +=1
        
print(time)