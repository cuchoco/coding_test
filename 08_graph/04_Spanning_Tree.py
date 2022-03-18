# 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 크루스칼 알고리즘: 최소한의 비용으로 신장 트리를 찾는법(최소 신장 트리 알고리즘)
# 모든 간선에 대해 정렬을 수행하고 가장 거리가 짦은 간선부터 포함 (그리디 알고리즘)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = 7, 9
parent = [i for i in range(v+1)]
input = [
    [1,2,29],
    [1,5,75],
    [2,3,35],
    [2,6,34],
    [3,4,7],
    [4,6,23],
    [4,7,13],
    [5,6,53],
    [6,7,25]
]

edges = []
result = 0

for edge in input:
    a,b,c = edge
    edges.append((c,a,b))

# 비용 오름차순 정렬 
edges.sort()

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함.
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(parent)
print(result)

