# https://www.acmicpc.net/problem/15686

from itertools import combinations

n, m = list(map(int, input().split()))
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

house_data = []
chicken_data = []

for i in range(len(data)):
    for j in range(len(data)):
        if data[i][j] == 1:
            house_data.append([i+1, j+1])
        elif data[i][j] == 2:
            chicken_data.append([i+1, j+1])

def get_distance(house, chicken):
    distance = 0
    for i_h, j_h in house:
        min_distance = 1e9
        for i_c, j_c in chicken:
            temp = abs(i_h - i_c) + abs(j_h - j_c)
            if temp < min_distance:
                min_distance = temp
        distance += min_distance
    return distance

min_distance = 1e9

for i in range(1, m+1):
    temp_chicken = list(combinations(chicken_data, i))
    for j in range(len(temp_chicken)):
        distance = get_distance(house_data, temp_chicken[j])
        if distance < min_distance:
            min_distance = distance

print(min_distance)