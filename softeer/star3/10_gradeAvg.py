import sys
n, k = list(map(int, sys.stdin.readline().split()))
scores = list(map(int, sys.stdin.readline().split()))
grades = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

# 단순 더하기
for grade in grades:
    start, end = grade
    count = end-start+1
    score = 0
    for i in range(start-1, end):
        score += scores[i]
    avg_score = score / count
    print(f'{avg_score:.2f}')


######################################
# 슬라이싱

for grade in grades:
    start, end = grade
    score = scores[start-1:end]
    score = sum(score) / len(score)
    print(f'{score:.2f}')