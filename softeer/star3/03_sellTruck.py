# 입력
# 5                       > 소비자 수
####소비자 제안 ####
# 제안개수 크기 가격
# 2 10 17 5 19
# 2 8 7 10 21
# 3 3 3 9 13 11 14
# 3 5 3 1 2 9 15
# 1 9 11
####################

# 시나리오 개수
# 11
# 시나리오 당 가격
# 21 31 35 54 79 80 100 3 5 7 9

# 출력 (최소 이정도 크기여야 시나리오당 가격 이상 매출)
# 5 8 9 9 10 11 -1 3 3 5 5


numBuyer = int(input())
offer = []   # [size, payment, buyerID]

for i in range(numBuyer):
    temp = list(map(int, input().split()))
    for j in range(temp[0]):
        offer.append([temp[2*j+1], temp[2*j+2], i+1])

numScenario = int(input())
temp = list(map(int, input().split()))
scenario = [] # [target_revenue, targetID, size(answer)]

for i in range(numScenario):
    scenario.append([temp[i], i+1])

offer.sort() #size
scenario.sort() #target_revenue

# print(offer)
# print(scenario)

revenue = 0
buyerPayment = [0] * (numBuyer+1)
sIndex = 0
for i in range(len(offer)):
    size = offer[i][0]
    payment = offer[i][1]
    buyerID = offer[i][2]

    if payment > buyerPayment[buyerID]:
        revenue += -buyerPayment[buyerID] + payment
        buyerPayment[buyerID] = payment
    
    while (sIndex < numScenario and scenario[sIndex][0] <= revenue):
        scenario[sIndex].append(size)
        sIndex += 1

while (sIndex < numScenario):
    scenario[sIndex].append(-1)
    sIndex += 1

scenario.sort(key=lambda x:x[1])

for i in scenario:
   print(i[2], end=' ')
    











        


        








