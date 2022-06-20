import sys

n, m = map(int, sys.stdin.readline().split())
map = []

for i in range(n):
    temp = list(sys.stdin.readline().rstrip())
    map.append(temp)

start_point = []
graph = [[] for _ in range(n*m)]
# 상하좌우
dy = [0,0,-1,1]
dx = [-1,1,0,0]


for y in range(n):
    for x in range(m):
        if map[y][x] == '#':
            temp = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if map[ny][nx] == '#':
                        temp += 1
            if temp == 1:
                start_point.append([y,x])


print(start_point)