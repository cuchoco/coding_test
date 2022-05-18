# 작업장의 수 N
# A 작업시간 B 작업시간 A > B 이동시간 B > A 이동시간
# A 작업시간 B 작업시간

# 입력
# 2
# 1 3 1 3
# 10 2

# 출력
# 4

import heapq

N = int(input())
graph = [[] for _ in range(2*(N+1) + 1)]

info = []
for i in range(N-1):
    A, B, AtoB, BtoA = list(map(int, input().split()))
    info.append([A,B])
    info.append([AtoB, BtoA])

info.append(list(map(int, input().split())))

for i in range(0,len(info),2):
    A, B = info[i]
    if i == 0:
        graph[1].append((3, A))  # A to A (1 > 3)
        graph[2].append((4, B))  # B to B (2 > 4)
    else:
        AtoB, BtoA = info[i-1]
        graph[i+1].append((i+3, A))      # (3 > 5)
        graph[i+2].append((i+4, B))      # (4 > 6)

        graph[i+1].append((i+4, B+AtoB)) # A to B (3 > 6)
        graph[i+2].append((i+3, A+BtoA))


def dijkstra(start):
    q = []

    # 시작 노드로 거리 0
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        # 최단거리 노드의 정보
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


# 1,2 에서 2N+1, 2N+2 의 최단거리중 최소
distance = [1e9] * len(graph)
dijkstra(1)
min_distance = min(distance[2*N+1], distance[2*N+2])

distance = [1e9] * len(graph)
dijkstra(2)
min_distance = min(distance[2*N+1], distance[2*N+2], min_distance)

print(min_distance)