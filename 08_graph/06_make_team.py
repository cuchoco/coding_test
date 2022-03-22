# 0~N 번까지의 번호 학생, 처음에는 N+1개의팀
# 선생님은 '팀 합치기', '같은 팀 여부 확인' 연산 사용가능.
# M개의 연산을 수행할 수 있을때 '같은팀 여부 확인' 연산에 대한 연산 결과 출력.
# 팀 합치기 연산 = (0,a,b)  같은팀 여부 확인 연산 = (1,a,b)

N, M = 7, 8

data = [
    (0,1,3),
    (1,1,7),
    (0,7,6),
    (1,7,1),
    (0,3,7),
    (0,4,2),
    (0,1,1),
    (1,1,1)
]

parent = [i for i in range(N+1)]

def find_parent(parent, x):
    # 루트 노드가 아니라면 찾을때까지 재귀적으로 호출
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(data):
    answer = []
    for oper, a, b in data:
        if oper == 0:
            union_parent(parent, a,b)
        if oper == 1:
            a = find_parent(parent, a)
            b = find_parent(parent, b)
            if a == b:
                answer.append('YES')
            else:
                answer.append('NO')
    
    return answer


answer = solution(data)

print(answer)