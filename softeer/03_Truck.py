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


n = int(input())
proposals = []
sizes = set()

for i in range(n):
    data = list(map(int,input().split(' ')))
    temp = []
    for j in range(1, len(data), 2):
        temp.append((data[j], data[j+1]))
        sizes.add(data[j])
    temp.sort(key=lambda x:x[0])
    proposals.append(temp)


# 1 3 5 8 9 10 11 인 경우만 확인
sizes = list(sizes)
sizes.sort()

sales = []
for size in sizes:
    sale = 0
    for proposal in proposals:
        max_sale = 0
        for i in range(len(proposal)):
            if size >= proposal[i][0]:
                if proposal[i][1] > max_sale:
                    max_sale = proposal[i][1]    

        sale += max_sale
    sales.append(sale)


n_price = int(input())
prices = list(map(int,input().split(' ')))

answer = []
for i in range(len(prices)):
    for j in range(len(sales)):
        if sales[j] >= prices[i]:
            idx = j
            break
        else:
            idx = -1
    
    if idx == -1:
        answer.append(-1)
    else:
        answer.append(sizes[idx])

for i in answer:
    print(i, end=' ')
    











        


        








