def binary_search(target, array):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start  + end) // 2
        if target == array[mid]:
            return mid
        # 중간 점보다 target이 큰 경우
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return None





target = 7
array = [1,3,4,5,7,9,11,13,15,17,19]

result = binary_search(target, array)

if result == None:
    print("원소가 존재하지 않음")

else:
    print(f"{result+1}번째에 있음")