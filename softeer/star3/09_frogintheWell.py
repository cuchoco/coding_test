import sys

N, M = list(map(int, sys.stdin.readline().split()))
limit = list(map(int, sys.stdin.readline().split())) #N 명의 한계 무개
res = [[i] for i in limit]
relations = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for i in range(M):
    a, b = relations[i]
    res[a-1].append(limit[b-1])
    res[b-1].append(limit[a-1])

count = 0
for i in res:
    if len(i) == 1:
        count += 1
    else:
        best = True
        for j in i[1:]:
            if j >= i[0]:
                best = False
                break
        if best:
            count += 1

print(count)


##############################

n, m = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))
g = [list(map(int, sys.stdin.readline().split())) for x in range(m)]

# [0] 리스트를 n+1개 만큼 만든다.
# 순서를 구분하기 위해 0번째의 수에 0을 넣어 제외한다.
cnt = [1 for _ in range(n+1)]
cnt[0]=0

# 그룹 수 만큼 반복한다.
# A,B가 들 수 있는 무게를 g 리스트에서 가져와 w에 넣어 비교한다.
# 비교할때 더 무거운 무게를 들 수 없다면 0을 부여한다.
for i in range(m):
    if w[g[i][0]-1] > w[g[i][1]-1]:
            cnt[g[i][1]] = 0

    elif w[g[i][0]-1] < w[g[i][1]-1]:
            cnt[g[i][0]] = 0

	# 똑같은 무게를 들 수 있다면 둘다 0을 부여
    else:
        cnt[g[i][0]] = 0
        cnt[g[i][1]] = 0


# cnt 리스트에 1의 개수를 출력한다.
print(cnt.count(1))