## 먹어야할 N개의 음식, 1~N 번호.
## 무지는 1초동안 음식을 먹고 다음 음식 먹음

food_times = [3,1,2]  # 음식 시간 배열
k = 5                 # 네트워크 장애 시간 (장애 시간 이후에 무엇을 먹어야 하는가)


############# 내답안 ###################    > 결과는 다 맞으니 효율성 실패
def solution(food_times, k):
    time = 0 
    while time != k+1:
        for i in range(len(food_times)):
            if food_times[i] == 0:
                if sum(food_times) == 0:
                    return -1
                
            else:
                food_times[i] -= 1
                time += 1
                
                if time == k+1:
                    return i+1

            
############## 책 답 (heapq 이용) ###############
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    # 시간이 적은 음식부터 빼기
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i], i+1))
        
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    
    length = len(food_times)
    
    while sum_value +((q[0][0] - previous)*length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다먹은 음식 제외
        previous = now # 이전 음식 시간 재설정
        
    result = sorted(q, key = lambda x:x[1])
    return result[(k-sum_value) % length][1]


############### 프로그래머스 #####################
def solution(ft, k):
    answer = 0

    while k > 0 :
        a = k // (len(ft) - ft.count(0) )
        b = k % (len(ft) - ft.count(0) )

        for i, j in zip(ft, range(len(ft))):
            if ft[j] != 0:
                ft[j] = i - a
                if ft[j] < 0:
                    b = b + abs(ft[j])
                    ft[j] = 0
            k = b

        if len(ft) - ft.count(0) ==0:
            return -1

        if k+1 <= len(ft) - ft.count(0):
            for i in ft:
                answer += 1
                if i !=0 :
                    k -= 1
                if k == -1:
                    return answer
                
        

print(solution(food_times,k))
