# BFS 예시 (Breadth) 넓이 우선 탐색
# DFS는 리스트와 재귀함수, BFS는 queue를 이용해서 구현한다.
from collections import deque

def maze(n,m, map):
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        # li = []
        # li.append((x,y))

        while queue:
            x, y = queue.popleft()

            # 현재 위치에서 네 방향으로의 위치 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 미로 찾기 공간을 벗어난 경우 무시
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                # 괴물인 경우 무시
                if map[nx][ny] == 0:
                    continue
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if map[nx][ny] == 1:
                    map[nx][ny] = map[x][y] + 1
                    queue.append((nx, ny))
        print(map)
        # 가장 오른쪽 아래까지의 최단 거리 반환
        return map[n-1][m-1] 

    return bfs(0,0)



n = 5
m = 6
map = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]

print(maze(n, m, map))