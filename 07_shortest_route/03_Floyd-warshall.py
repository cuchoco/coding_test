# 다익스트라는 '한 지점에서 다른 특정 지점까지의 최단경로' 를 구하는 경우 씀.
# 플로이드는 '모든 지점에서 다른 모든 지점까지의 최단경로' 를 모두 구해야 하는 경우에 사용.
# 2차원 리스트에 '최단거리' 정보를 저장하는 특징.

INF = int(1e9)
n = 4 
m = 7
graph = [[INF]*(n+1) for _ in range(n+1)]
edge = [
    [1,2,4],
    [1,4,6],
    [2,1,3],
    [2,3,7],
    [3,1,5],
    [3,4,4],
    [4,3,2]
]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0


# 각 간선의 정보 graph에 대입.
for i in range(m):
    a, b, c = edge[i]
    graph[a][b] = c

# 점화식에 따라 플로이스 워셜 알고리즘 수행.
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# 수행 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()



