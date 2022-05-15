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

n = len(key)
m = len(lst)

for i in range(n):
    row = i // 5 
    col = i % 5
    matrix[row][col] = key[i]

for i in range(n, m+n):
    row = i // 5
    col = i % 5
    matrix[row][col] = lst[i-n]




