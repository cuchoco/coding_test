import sys
n, k = list(map(int, sys.stdin.readline().split()))
strings = list(sys.stdin.readline())
count = 0

for i in range(n):
    if strings[i] == 'P':
        for j in range(i-k, i+k+1):
            if j < 0 or j > n-1:
                continue
            elif strings[j] == 'H':
                strings[j] = 'X'
                count += 1
                break

print(count)