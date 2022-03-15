# 개선된 다익스트라 알고리즘에서는 힙(heap) 자료구조를 사용.
# 최단거리에 대한 정보를 힙에 담아서 처리. 우선순위 큐 > PriorityQueue 혹은 heapq 사용.
# 힙은 완전 이진트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조.
 
# 다익스트라 알고리즘에서는 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용.
# get_smallest_node() 라는 함수 필요하지 않음.
import heapq

INF = int(1e9)

n = 6      # 노드의 개수
m = 11     # 간선의 개수
start = 1  # 시작 노드 번호

graph = [[] for i in range(n+1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트.

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


def dijkstra(start):
    q = []

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해 큐에 삽입.
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist+ i[1]

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)


# 모든 노드로 가기 위한 최단거리
for i in range(1, n+1):
    if distance[i] == INF:
        print("Inf")
    else:
        print(f'{i}번 노드로 가는 최소 비용:', distance[i])
