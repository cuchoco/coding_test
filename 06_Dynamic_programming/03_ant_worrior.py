# 식량창고 일직선, 한칸이상 떨어진 식량창고 약탈
# ex {1, 3, 1, 5} > 2번째와 4번째 식량창고를 선택했을때 최대값
# 식량창고 N개가 주어졌을때의 얻는 식량의 최대값 구하는 프로그램.

# Bottom up

from pandas import array


x = (1,3,1,5)

# i-1 번째를 터는 경우 i 번째를 털 수 없음.
# i-2 번째를 터는 경우 i 번째를 털 수 있음.

def answer(array):
    n = len(array)

    d = [0] * 100
    d[0] = array[0]
    d[1] = max(array[0], array[1])
    for i in range(2, n):
        d[i] = max(d[i-1], d[i-2] + x[i])


    return(d[n-1]) # n개를 털때의 가장 높은 식량

print(answer(x))
