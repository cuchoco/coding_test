# 00시 00분 00초 부터 N시 59분 59초 까지 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램

def cases(n:int) -> int:
    count = 0
    
    times = range(0, n+1)
    minutes = range(0,60)
    seconds = range(0,60)
    for time in times:
        for minute in minutes:
            for second in seconds:
                target =str(time) + str(minute) + str(second)
                if '3' in target:
                    count += 1
    return count




if __name__ =="__main__":
    print(cases(5))