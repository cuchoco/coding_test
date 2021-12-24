# stack
stack = []

# 5 - 2 - 3 - 7 - del - 1 - 4 - del
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4) 
stack.pop()

print('stack: ', stack)

# queue
from collections import deque

queue = deque()

# 5 - 2 - 3 - 7 - del - 1 - 4 - del
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print('queue: ', queue)