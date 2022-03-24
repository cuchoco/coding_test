N = 5
data = [2,3,1,2,2]

# 공포도가 x인 모험가는 반드시 x명 이상으로 구성. 그룹 구성 최대값은?
def solution(data):
    data.sort()    # [1,2,2,2,3]
    count = 0
    result = 0
    
    for i in data:
        # 한명씩 그룹에 추가
        count += 1

        # 그룹의 인원이 현재 모험가의 공포도를 넘어서면, 그룹 결성        
        if count >= i:
            result += 1
            count = 0

    return result


print(solution(data))