# 판매원 A는 현재 1번 회사에 위치해 있으며 X번 회사에 방문해 물건을 팔고자 한다.
# 도로가 연결되어 있다면 1만큼의 시간으로 이동가능. 
# 소개팅 상태는 K번 회사에 존재. 
# A의 동선 1번 > K번 > X번. 회사 사이를 이동하는 최소 시간을 계산하는 프로그램 작성.
# 플로이드 워셜

n = 5
m = 7
k = 5
x = 4
INF = int(1e9)

def solution():
    edge = [[1,2,1],[1,3,1],[1,4,1],[2,4,1],[3,4,1],[3,5,1],[4,5,1]]
    
    graph = [[INF]*(n+1) for _ in range(n+1)]
    
    # 자기 자신 비용 초기화
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b: graph[a][b] = 0

    # 간선정보 초기화
    for i in range(m):
        a,b,c = edge[i]
        # 양방향 이동 가능
        graph[a][b] = c
        graph[b][a] = c
    
    # 점화식 이용
    for k in range(1,n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    return graph

graph = solution()

distance = graph[1][k] + graph[k][x]

print("-1") if distance == INF else print(distance)
