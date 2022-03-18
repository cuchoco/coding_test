# 특정 원소가 속한 집합 찾기.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 유니온 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = 3, 3
unions = [
    [1,2],
    [1,3],
    [2,3],
]
parent = [i for i in range(v+1)]
cycle = False

for i in range(e):
    a, b = unions[i]

    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break

    else:
        union_parent(parent, a, b)


print(parent)

if cycle:
    print("사이클")
else:
    print("사이클 x")

