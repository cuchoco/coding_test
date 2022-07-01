# https://programmers.co.kr/learn/courses/30/lessons/92341

from collections import defaultdict
from math import ceil

def solution(fees, records):
    data = defaultdict(list)
    for record in records:
        time, car_id, status = record.split()
        time =  int(time.split(':')[0]) * 60 + int(time.split(':')[1])  # 시간을 10진수로 변환
        data[car_id].append((time))                                     
    
    for key in data.keys(): 
        # 홀수인경우 in만 남았으므로 마지막 시간 더해줌
        if len(data[key]) % 2 == 1:
            data[key].append((23*60 + 59))

    # 순서대로 출력하기위해 sorting
    data = sorted(data.items(), key = lambda x: x[0])
    
    answer = []
    
    for _, times in data:
        parking_time = 0
        for i in range(len(times)//2):
            parking_time += times[2*i+1] - times[2*i]
        
        # 기본요금 부여
        if parking_time <= fees[0]:
            answer.append(fees[1])
        
        # 기본시간을 넘는 경우
        else:
            answer.append(fees[1] + ceil((parking_time-fees[0])/fees[2]) *fees[3])
        
    return answer