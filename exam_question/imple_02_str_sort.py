# 알파벳 오름차순 정렬하고 숫자는 더해서 마지막에 추가

data1 = 'K1KA5CB7'
data2 = 'AJKDLSI412K4JSJ9D'

def solution(data):
    data = list(data)
    data.sort()
    num = 0
    result = []
    for x in data:
        if 48 <= ord(x) <=57:
            num += int(x)
        else:
            result.append(x)

    return ''.join(result) + str(num)

print(solution(data1))
print(solution(data2))