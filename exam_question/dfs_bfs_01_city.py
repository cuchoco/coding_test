# n개 도시 m개 도로 도로 거리는 1
# 도시 x 로부터 출발해 최단거리가 정확히 k인 도시의 번호를 출력

from collections import deque
import sys
f = sys.stdin.readline

n, m, k, x = list(map(int, f().split()))
graph = [[] for _ in range(n+1)] 
distance = [1e9] * (n+1)
visited = [False] * (n+1)

for i in range(m):
    a, b = list(map(int, f().split()))
    graph[a].append(b)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    distance[start] = 0

    while queue:
        v= queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]= True
                distance[i] = distance[v] + 1

bfs(x)

answer = []
for i in range(len(distance)):
    if distance[i] == k:
        answer.append(i)

if answer:
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)