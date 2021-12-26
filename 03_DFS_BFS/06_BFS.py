# 너비 우선 탐색: 가까운 노드부터 탐색하는 알고리즘
# 선입선출 방식인 큐 자료구조를 이용.
from collections import deque

# BFS 메서드 정의 
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v= queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]= True

# 인접 리스트
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보
visited = [False] * 9

# bfs 함수 호출
bfs(graph, 1, visited)