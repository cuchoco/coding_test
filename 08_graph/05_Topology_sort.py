# 위상정렬: 정렬 알고리즘.
# 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는것'

from collections import deque

v, e = 7, 8

edge = [
    [1,2],
    [1,5],
    [2,3],
    [2,6],
    [3,4],
    [4,7],
    [5,6],
    [6,4]
]

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)

# 간선 정보를 담기위한 연결리스트
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선정보 입력받기

for i in range(e):
    a, b = edge[i]
    graph[a].append(b)  # a 에서 b 로 가는 간선
    
    # 진입 차수 증가
    indegree[b] += 1   # b로 들어오는 간선 +1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기.
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0 이되는 노드를 큐에 삽입.
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')
    print()

topology_sort()

        

