#왼쪽부터 오른쪽까지 모든 숫자를 확인해 +나 x를 이용해 가장 큰수를 만들어라 

data = '02984'

result = 1

for i in data:
    if int(i) == 0:
        result += int(i)

    else:
        result *= int(i)

print(result)