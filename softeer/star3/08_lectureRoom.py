import sys
from heapq import heapify, heappop

nLecture = int(sys.stdin.readline())
lst = []
for i in range(nLecture):
    start, end = list(map(int, sys.stdin.readline().split()))
    lst.append((end, start))

heapify(lst)

now = 0
count = 0

while lst:
    end, start = heappop(lst)
    if start >= now:
        count += 1
        now = end
    
print(count)