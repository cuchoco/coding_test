# 볼링공의 갯수 N, 존재하는 무개 M
# 두 사람은 서로 무게가 다른 볼링공을 고르고자함.
# 볼링공 번호 조합의 개수는?


data = [1,3,2,3,2]
data = [1,5,4,3,2,4,5,2]

N = len(data)
result = 0

for i in range(N):
    for j in data[i+1:]:
        if data[i] != j:
            result += 1

print(result)