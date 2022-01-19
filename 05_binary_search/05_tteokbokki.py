# 떡의개수 N, 요청한 떡의 길이 M
# 떡의 개별 높이 주어짐, 적어도 M만큼의 떡을 얻기 위해 절단기에 설정하는 최대높이는?
N = 4 
M = 6
array = [19, 15, 10, 17]

def cutting(array, M):
    max_heigt = min(array)
    
    while True:
        tail = 0
    
        for i in array:
            if i > max_heigt:
                tail += (i - max_heigt)

        if tail <= M:
            return max_heigt

        else:
            tail = 0
            max_heigt += 1
        



print(cutting(array, M))


    
