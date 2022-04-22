# 기본 이진 탐색
def binarySearch(start, end, key):
    while start <= end:
        mid = (start + end) // 2

        if lst[mid] > key:
            end = mid - 1

        elif lst[mid] < key:
            start = mid + 1

        elif lst[mid] == key:
            return mid

    return 0
    

def lowerBound(start, end, key):
    while start < end:
        mid = (start + end) // 2

        if lst[mid] >= key:
            end = mid

        elif lst[mid] < key:
            start = mid + 1

    return end
    



def upperBound(start, end, key):
    while start < end:
        mid = (start + end) // 2

        if lst[mid] <= key:
            start = mid + 1

        elif key < lst[mid]:
            end = mid

    return end
    




lst = [0, 1, 3, 3, 4, 5, 6, 6, 9, 10]

print(binarySearch(0, len(lst)-1, 7))  # 7이 없으므로: 0
print(lowerBound(0, len(lst), 7)) # 7이거나 7보다 큰값이 나오는 첫번째 위치: 8
print(upperBound(0, len(lst), 6)) # 처음으로 6보다 큰값이 나오는 위치 : 8
