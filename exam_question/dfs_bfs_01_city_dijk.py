# n개 도시 m개 도로 도로 거리는 1
# 도시 x 로부터 출발해 최단거리가 정확히 k인 도시의 번호를 출력
import heapq

n, m, k, x = list(map(int, input().split()))
data = []
for i in range(m):
    temp = list(map(int, input().split()))
    data.append(temp+[1])

distance = [1e9] * (n+1)
graph = [[] for _ in range(n+1)]

for i,j,c in data:
    graph[i].append((j, c))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q) 
        if distance[now] < dist:
            continue
        
        # 현재 노드와 근접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 가는 비용이 더 낮을 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(x)

answer = []

for i in range(len(distance)):
    if distance[i] == k:
        answer.append(i)

answer.sort()

if answer:
    for i in answer:
        print(i)

else:
    print(-1)

