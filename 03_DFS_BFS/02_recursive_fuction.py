def recursive_func1():
    print('재귀 함수를 호출 합니다')
    recursive_func1()

    
try:
    recursive_func1()
except:
    print("재귀함수 오류 종료")
    pass


def recursive_func2(i):
    if i == 100 :
        print("100번째 재귀함수입니다")
        return 
    print(i,f"번째 재귀함수에서 {i+1}번째 재귀 함수를 호출합니다.")
    recursive_func2(i+1)
    print(i, '번째 재귀함수를 종료합니다')

recursive_func2(1)