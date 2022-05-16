lenNum = int(input())
cases = []
for i in range(lenNum):
    src, dst = list(input().split())
    cases.append((src, dst))

na = [0,0,0,0,0,0,0]

myMatrix = [[1,1,1,0,1,1,1],  # 0 1 2 3 4 5 6 7 8 9
            [0,0,1,0,1,0,0],
            [0,1,1,1,0,1,1],
            [0,1,1,1,1,1,0],
            [1,0,1,1,1,0,0],
            [1,1,0,1,1,1,0],
            [1,1,0,1,1,1,1],
            [1,1,1,0,1,0,0],
            [1,1,1,1,1,1,1],
            [1,1,1,1,1,1,0]]

for i in cases:
    src, dst = i
    src = list(map(int,src))
    dst = list(map(int,dst))
    if len(src) > len(dst):
        for _ in range(len(src)-len(dst)):
            dst.insert(0, 'na')

    if len(src) < len(dst):
        for _ in range(len(dst)-len(src)):
            src.insert(0, 'na')
    
    count = 0
    for j, k in zip(src, dst):
        if j == 'na':
            j = na
        else:
            j = myMatrix[j]
        if k == 'na':
            k = na
        else:
            k = myMatrix[k]

        for a,b in zip(j,k):
            if (a ^ b):
                count +=1

    print(count)