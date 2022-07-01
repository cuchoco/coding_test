# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, cols, queries):
    mat = [[i + cols*j for i in range(1, cols+1)] for j in range(rows)]
    answer = []
    
    for query in queries:
        r_1, c_1, r_2, c_2 = query
        r_min, c_min, r_max, c_max = r_1 - 1, c_1 - 1, r_2 - 1, c_2 - 1

        coordinates = []
        # 출발 > 오
        for i in range(c_min, c_max):
            coordinates.append((r_min, i))
        # 오 > 밑
        for i in range(r_min, r_max):
            coordinates.append((i, c_max))
        # 밑 > 왼
        for i in range(c_max, c_min, -1):
            coordinates.append((r_max, i))
        # 왼 > 위
        for i in range(r_max, r_min, -1):
            coordinates.append((i, c_min))

        numbers = [mat[row][col] for row, col in coordinates]
        answer.append(min(numbers))

        numbers.insert(0, numbers.pop())

        for i in range(len(coordinates)):
            row, col = coordinates[i]
            mat[row][col] = numbers[i]
    
    
    return answer

######### deque rotate 사용 #########

from collections import deque

def solution(rows, cols, queries):
    mat = [[i + cols*j for i in range(1, cols+1)] for j in range(rows)]
    answer = []
    
    for query in queries:
        r_1, c_1, r_2, c_2 = query
        r_min, c_min, r_max, c_max = r_1 - 1, c_1 - 1, r_2 - 1, c_2 - 1

        coordinates = []
        # 출발 > 오
        for i in range(c_min, c_max):
            coordinates.append((r_min, i))
        # 오 > 밑
        for i in range(r_min, r_max):
            coordinates.append((i, c_max))
        # 밑 > 왼
        for i in range(c_max, c_min, -1):
            coordinates.append((r_max, i))
        # 왼 > 위
        for i in range(r_max, r_min, -1):
            coordinates.append((i, c_min))

        numbers = deque([mat[row][col] for row, col in coordinates])
        answer.append(min(numbers))
        numbers.rotate(1)

        for i in range(len(coordinates)):
            row, col = coordinates[i]
            mat[row][col] = numbers[i]
    
    
    return answer