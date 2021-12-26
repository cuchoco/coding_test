# Depth-first Search

# Adjacency Matrix: 2차원 배열로 그래프의 연결관계를 표현하는 방식.
# adjacency list: 리스트로 그래프의 연결관계를 표현하는 방식. 

# 1. 인접행렬 방식: 2차원 리스트를 이용해 인접행렬 표현
INF = float('inf') 
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
print("인접 행렬", graph)
print()

# 2. 인접리스트 방식: 행이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

#노드 1에 연결된 노드 정보 저장
graph[1].append((0, 7))

# 노드 2
graph[2].append((0, 5))

print("인접 리스트", graph)