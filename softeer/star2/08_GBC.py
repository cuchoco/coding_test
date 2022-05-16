from collections import deque

N, M = list(map(int, input().split()))

restrict = deque([])
test = deque([])

for i in range(N):
    length, speed = list(map(int, input().split()))
    restrict.append((length, speed))

for i in range(M):
    length, speed = list(map(int, input().split()))
    test.append((length, speed))

max_speed = 0 
test_length = 0
restrict_length = 0

while (test or restrict):
    if test_length > restrict_length:
        r_length, r_speed = restrict.popleft()
        restrict_length += r_length
        max_speed = max(max_speed, t_speed - r_speed)

    elif test_length < restrict_length:
        t_length, t_speed = test.popleft()
        test_length += t_length
        max_speed = max(max_speed, t_speed - r_speed)
        
    else:
        r_length, r_speed = restrict.popleft()
        t_length, t_speed = test.popleft()
        test_length += t_length
        restrict_length += r_length
        max_speed = max(max_speed, t_speed - r_speed)

print(max_speed)
