# 동전을 가지고 만들수 없는 양의 정수중 최솟값

############# 내 답안 #############    # 답은 나오지만 정답에 비해 복잡.
from itertools import combinations

data = [3,2,1,1,9]
N = len(data)
result = [False] * 10000

for i in range(1, N+1):
    lst = combinations(data, i)
    for j in lst:
        j = sum(j)    
        result[j] = True

for idx,i in enumerate(result[1:], start=1):
    if i == False:
        print(idx)
        break


################## 정답(그리디 알고리즘) #####################

data = [3,2,1,1,9]
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)