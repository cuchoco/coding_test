# https://programmers.co.kr/learn/courses/30/lessons/42888

from collections import defaultdict

def solution(record):
    answer = []
    uid_name = defaultdict()
    for string in record:
        temp = string.split()
        if temp[0] == 'Enter':
            uid_name[temp[1]] = temp[2]
            answer.append(('Enter', temp[1]))
            
        elif temp[0] == 'Change':
            uid_name[temp[1]] = temp[2]
            
        else:
            answer.append(('Leave', temp[1]))
    
    result = []
    for act, uid in answer:
        if act == 'Enter':
            temp = uid_name[uid] + "님이 들어왔습니다."
            result.append(temp)
        else:
            temp = uid_name[uid] + "님이 나갔습니다."
            result.append(temp)
            
    return result