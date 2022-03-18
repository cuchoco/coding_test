# 경로 압축 기법
# find 함수를 재귀적으로 호출한다음 부모테이블을 갱신. 
# 루트노드를 찾음 (본인, 본인) 
def find_parent(parent,x):
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
 

# 노드(v) 간선(e) 의 개수
v, e = 6, 4
parent = [i for i in range(v+1)] # 부모테이블(자기 자신을 부모로 가지는) 초기화

unions = [
    [1,4],
    [2,3],
    [2,4],
    [5,6]
]

for i in range(e):
    a, b = unions[i]
    union_parent(parent,a, b)

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