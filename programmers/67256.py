# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = []
    leftPosition = [3, 0]
    rightPosition = [3, 2]
    
    for num in numbers:
        if num == 0:
            num = 11
            
        if num in [1, 4, 7]:
            answer.append('L')
            leftPosition = [(num-1) // 3, (num-1) % 3]
            
        elif num in [3, 6, 9]:
            answer.append('R')
            rightPosition = [(num-1) // 3, (num-1) % 3]
            
        else:
            numPosition = [(num-1) // 3, (num-1) % 3]
            leftDistance = abs(leftPosition[0] - numPosition[0]) + abs(leftPosition[1] - numPosition[1])
            rightDistance = abs(rightPosition[0] - numPosition[0]) + abs(rightPosition[1] - numPosition[1])

            if leftDistance < rightDistance:
                answer.append('L')
                leftPosition = numPosition
            elif leftDistance > rightDistance:
                answer.append('R')
                rightPosition = numPosition
            else:
                if hand == 'right':
                    answer.append('R')
                    rightPosition = numPosition
                else:
                    answer.append('L')
                    leftPosition = numPosition
                    
    return ''.join(answer)