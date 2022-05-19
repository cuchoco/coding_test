nStone = int(input())
stoneList = list(map(int, input().split()))

dp = [1] * nStone

for i in range(1, nStone):
    for j in range(i):
        if stoneList[i] > stoneList[j]: # 선택한 돌이 이 전의 돌보다 높다면
            dp[i] = max(dp[i], dp[j]+1) # (이전에 돌을 가장 많이 밟은 방법 + 1)
        print(dp)

print(max(dp))