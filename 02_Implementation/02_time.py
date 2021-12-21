# 00시 00분 00초 부터 N시 59분 59초 까지 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램

def cases(n:int) -> int:
    count = 0    
    for time in range(0, n+1):

        for minute in range(0,60):

            for second in range(0,60):
                if '3' in str(time) + str(minute) + str(second):
                    count += 1
    
    return count




if __name__ =="__main__":
    print(cases(5))