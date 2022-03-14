# 다익스트라, 플로이드워셜, 벨만 포드 알고리즘 등등 이있다.
# 다익스트라: 음의 간선이 없을때 정상적으로 작동.
# 각 노드에 대한 현재까지의 최단거리 정보를 항상 1차원 리스트에 저장하며 갱신.
# 그리디 알고리즘 및 다이나믹 프로그래밍의 한 종류임

INF = int(1e9) # 무한 10억

n = 6      # 노드의 개수
m = 11     # 간선의 개수
start = 1  # 시작 노드 번호

graph = [[] for i in range(n+1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트.
visited = [False] * (n+1)

# 최단 거리 테이블
distance = [INF] * (n+1)


# 모든 간선 정보 입력
edge = [
    [1,2,2],   # 1번 노드에서 2번노드로 가는 비용은 2 라는뜻
    [1,3,5],
    [1,4,1],
    [2,3,3],
    [2,4,2],
    [3,2,3],
    [3,6,5],
    [4,3,3],
    [4,5,1],
    [5,3,1],
    [5,6,2]   
]


for i in range(m):
    a, b, c = edge[i]
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 최단거리가 짧은 노드의 번호를 반환.
def get_smallest_node():
    min_value = INF
    index = 0 
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i         
    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True

    # start 노드에서 갈수있는 다른 노드의 거리 입력.
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복

    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]    
            if cost < distance[j[0]]:     
                distance[j[0]] = cost

