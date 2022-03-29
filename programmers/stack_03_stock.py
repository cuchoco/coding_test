# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.
# 입출력 예
# prices	return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
# 입출력 예 설명
# 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
# 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
# 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
# 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

########################## 내답안 ################################## > 효율성 테스트 실패
def solution(prices):
    answer = []
    
    for idx, i in enumerate(prices):
        time = 0
        for j in (prices[idx+1:]):
            time += 1
            
            # 만약 떨어지면 정지.
            if j < i:
                answer.append(time)
                break 
        
        if j >= i:    
            answer.append(time)

    return answer

#################### 내 답안2 ######################### > 효율성 개선 but 여전히 실패

def solution(prices):
    answer = []
    for _ in range(len(prices)):
        price = prices.pop(0)
        
        # 가격이 떨어 지는 경우가 True
        pivot = [i < price for i in prices]

        if any(pivot): # 있는 경우
            answer.append(pivot.index(True)+1)
        else:
            answer.append(len(prices))
            
    return answer

################## 답안 3 #######################

def solution(prices):

    result=[0 for x in range(len(prices))]

    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]<=prices[j]:
                result[i]+=1
            else:
                result[i]+=1
                break
    return result

