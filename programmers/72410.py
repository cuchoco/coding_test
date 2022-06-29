# https://programmers.co.kr/learn/courses/30/lessons/72410

import re
regex = re.compile("[0-9a-z\.\_\-]")

def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = re.findall(regex, new_id)
    if len(new_id) == 0:
        new_id = 'a'
    # 3단계
    temp = [0]
    for i in new_id:
        if i == '.' and temp[-1] == '.':
            pass
        else:
            temp.append(i)
    temp.pop(0)
    # 4단계
    if temp[0] == '.':
        temp.pop(0)
    if len(temp) > 0:
        if temp[-1] == '.':
            temp.pop()
    # 5단계
    if len(temp) == 0:
        temp.append('a')
    # 6단계
    if len(temp) >= 16:
        temp = list(temp)[:15]
        if temp[-1] == '.':
            temp.pop()
    # 7단계
    if len(temp) <= 2:
        value = temp[-1]
        while len(temp) != 3:
            temp.append(value)
    return ''.join(temp)