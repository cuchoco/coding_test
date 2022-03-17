# 서로소 집합(공통 원소가 없는 두 집합), 서로소 집합 자료구조는 union, find 2개의 연산으로 조작할수있다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니면, 루트 노드를 찾을 때 까지 재귀적으로 호출. > 자기자신이 부모인것이 루트노드
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드(v) 간선(e) 의 개수
v, e = 6, 4
parent = [i for i in range(v+1)] # 부모테이블(자기 자신을 부모로 가지는) 초기화

unions = [
    [1,4],
    [2,3],
    [2,4],
    [5,6]
]

# union 연산 수행
for i in range(e):
    a, b = unions[i]
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end='')
for i in range(1, v+1):
    print(find_parent(parent,i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블:', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

print()