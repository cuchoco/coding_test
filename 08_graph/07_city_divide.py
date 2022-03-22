# n: 집의개수 m: 길의 개수.
# 길은 양방향, 유지비 존재. 마을을 2개로 분리할 계획.
# 분리된 두 마을 사이의 길은 없애고, 분리된 마을 안에서는 경로가 존재하며 유지비 최소.

# N: 집의 개수 M: 길의 개수 
# [A,B,C] : A번과 B번집을 연결하는 길의 유지비가 C

N, M = 7 ,12
data =[
    [1,2,3],
    [1,3,2],
    [3,2,1],
    [2,5,2],
    [3,4,4],
    [7,3,6],
    [5,1,5],
    [1,6,2],
    [6,4,1],
    [6,5,3],
    [4,5,3],
    [6,7,4]
]

# 최소 신장 트리를 찾고 가장 값이 큰 간선을 제거하면 2개의 최소 신장 트리 생성.(크루스칼 알고리즘)

parent = [i for i in range(N+1)]


def find_parent(parent, x):
    if parent[x] != x:         
        parent[x] = find_parent(parent, parent[x])
    return parent[x]  # 자기 자신이 부모인 노드: 루트노드

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(data):
    edges = []    # 간선정보
    for a,b,cost in data:
        edges.append((cost,a,b))
    edges.sort()

    result = 0
    last = 0
    for cost,a,b in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            last = cost
    
    return result - last


print(solution(data))
