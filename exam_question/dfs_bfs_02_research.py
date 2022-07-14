#https://www.acmicpc.net/problem/14502

import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

f = sys.stdin.readline
n, m = list(map(int, f().split()))  
data = []
zero = []

for i in range(n):
    temp = list(map(int, f().split()))
    data.append(temp)
    for j in range(m):
        if temp[j] == 0:
            zero.append((i, j))

def virusSenerio(data):
    queue = deque([])
    
    visited = [[False] * m for _ in range(n)]
    # 상 하 좌 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for y in range(n):
        for x in range(m):
            if data[y][x] == 2 and not visited[y][x]:
                queue.append((y,x))

                while queue:
                    temp_y, temp_x = queue.popleft()
                    visited[temp_y][temp_x] = True

                    # 네 방향 확인
                    for k in range(4):
                        ny = temp_y + dy[k]
                        nx = temp_x + dx[k]

                        if (0<= ny < n and 0 <= nx < m) and data[ny][nx] == 0 and not visited[ny][nx]:
                            queue.append((ny, nx))
                            data[ny][nx] = 2
    return data


comb = list(combinations(zero, 3))
max_zero = 0

for lst in comb:
    temp = deepcopy(data)
    zero = 0
    for y, x in lst:
        temp[y][x] = 1

    temp = virusSenerio(temp)

    for y in range(n):
        for x in range(m):
            if temp[y][x] == 0:
                zero += 1
    
    if max_zero < zero:
        max_zero = zero

print(max_zero)







