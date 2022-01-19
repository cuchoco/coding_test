N = 4 
M = 6
array = [19, 15, 10, 17]

def cutting(array, M):
    array.sort()
    start = 0
    end = max(array)

    # 이진 탐색 수행
    result = 0
    while (start <= end):
        total = 0
        mid = (start + end) // 2
        
        for x in array:
            # 잘랐을 때의 떡의 양 계산
            if x > mid:
                total += x - mid
        # 떡의 양이 부족한 경우 더 많이 자르기(끝점을 중간점-1로 옮김)
        if total < M:
            end = mid -1
        # 떡의 양이 충분한 경우 덜 자르기(시작점을 중간점+1로 옮김)
        else:
            result = mid 
            start = mid + 1
        
    return result



print(cutting(array, M))
