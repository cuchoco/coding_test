import heapq

W, N = list(map(int, input().split()))
treasures = []
for i in range(N):
    weight, price = list(map(int, input().split()))
    heapq.heappush(treasures, (-price, weight))
    
revenue = 0

while W > 0:
    price, weight = heapq.heappop(treasures)

    if W > weight:
        W -= weight
        revenue += -price*weight
    else:
        revenue += -price*W
        W = 0
        
print(revenue)