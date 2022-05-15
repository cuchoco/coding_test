# HELLOWORLD
# PLAYFAIRCIPHERKEY


message = list(input())
key = list(input())

lst = list(map(chr, range(65, 91)))
lst.remove('J')

matrix = [[0]*5 for i in range(5)]

for i in range(len(key)):
    for j in range(i+1, len(key)):
        if key[i] == key[j]:
            key[j] = -1

key = [i for i in key if i != -1]

for i in key:
    lst.remove(i)

key = key + lst


for i in range(len(key)):
    row = i // 5 
    col = i % 5
    matrix[row][col] = key[i]


new_message = []
while message:
    temp0 = message.pop(0)
    if len(message) == 0:
        new_message.append([temp0, 'X'])
        break

    temp1 = message.pop(0)

    if temp0 != temp1:
        new_message.append([temp0, temp1])
    
    elif temp0 == temp1 and temp0=='X':
        new_message.append(['X','Q'])
        message.insert(0, temp1)

    elif temp0 == temp1:
        new_message.append([temp0, 'X'])
        message.insert(0, temp1)


return_message = []

for arr in new_message:
    temp0, temp1 = arr
    idx0 = key.index(temp0)
    idx1 = key.index(temp1)

    row0 = idx0 // 5
    col0 = idx0 % 5

    row1 = idx1 // 5
    col1 = idx1 % 5

    # 같은 행인 경우
    if row0 == row1:
        col0 = (col0 + 1) % 5 
        col1 = (col1 + 1) % 5

    # 같은 열인 경우
    elif col0 == col1:
        row0 = (row0 + 1) % 5 
        row1 = (row1 + 1) % 5
    
    # 둘다 아닌경우
    else:
        col0, col1 = col1, col0

    
    temp0 = matrix[row0][col0]
    temp1 = matrix[row1][col1]

    return_message += [temp0 + temp1]


print(''.join(return_message))

    






    
        
    

    



    

