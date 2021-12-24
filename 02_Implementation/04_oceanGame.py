
def game(n,m, loc_data, map_data):
    x, y, head = loc_data
    d = [ [0] * m for _ in range(n) ]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    d[x][y] = 1 #현재 좌표 방문처리
    count = 1

    # 왼쪽으로 회전
    def turn_left(head):
        head -= 1
        if head == -1:
            head = 3
        return head

    # 시뮬레이션 시작
    turn_time = 0
    while True:
        head = turn_left(head)
        nx = x + dx[head]
        ny = y + dy[head]

        # 회전 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
        if d[nx][ny] == 0 and map_data[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        # 회전 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
        else:
            turn_time += 1

        # 네 방향 모두 갈 수 없는 경우
        if turn_time == 4:
            nx = x - dx[head]
            ny = y - dy[head]
            
            # 뒤로 갈 수 있다면 이동
            if map_data[nx][ny] == 0:
                x = nx
                y = ny
            # 뒤가 바다로 막혀있는 경우
            else:
                break
    
            turn_time = 0
    return count

map = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1]
]
print(game(4,4,(1,1,0),map))

    
            





    