# N개의 도시가 존재. 다른도시로 전보를 보내서 메시지 전달 가능
# C라는 도시에서 위급 상황 발생. 각 도시 사이 설치된 통로를 거쳐 최대한 많이 퍼져나감.
# 각 도시의 번호와 통로가 설치되어있는 정보가 주어졌을때.
# 도시 C에서 보낸 메세지를 받게되는 도시의 개수는 총 몇개이며 메세지를 받는데까지 걸리는 시간은?

import heapq

N = 3
M = 2
C = 1
INF = int(1e9)

edge = [[1,2,4],[1,3,2]]
distance = [INF] * (N+1)


graph = [[] for _ in range(N+1)]

for i in range(M):
    a,b,c = edge[i]
    graph[a].append((b,c))   # a 번째 도시에 (b, c) 이어진 b라는 도시에 전보가 걸리는 시간은 c

def dijkstra(start):
    
    # 시작 위치에서 정보 초기화
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)   
        
        # 방문한 노드 무시 처리. 
        if distance[now] < dist: 
            continue

        # 연결된 노드 확인
        for i in graph[now]:                  # i[0]: 연결된 노드  i[1]: 연결노드 방문비용
            cost = dist + i[1]

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)

count = 0
max_time = 0

for i in distance:
    if i == INF:
        continue
    if i > 0: count += 1
    if i > max_time: max_time = i


print("메세지를 받는 도시의 수:", count)
print("총 걸리는 시간:", max_time)