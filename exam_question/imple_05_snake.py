# https://www.acmicpc.net/problem/3190
# 뱀이 사과를 먹으면 몸의 길이가 늘어남. 자기자신의 몸이나 벽에 부딪히면 게임이 끝남.
# 맨위 맨좌측에 위치. 뱀의 길이는 1이며 처음에 오른쪽을 향함
# 뱀은 매초마다 이동
# 1. 몸길이를 늘려 머리를 다음칸에 위치.
# 2. 이동한 칸에 사과가 없으면 꼬리가 위치한 칸을 비움
# 3. 사과가 있다면 사과가 없어지고 꼬리는 움직이지않음
# 사과의 위치와 뱀의 이동경로가 주어질때 이 게임이 몇초에 끝나는지 계산

# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 
# 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. 
# X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.


N = 6   # 보드의 크기 
K = 3   # 사과의 개수
L = 3   # 뱀의 방향 변환 횟수
apple = [[3,4],[2,5],[5,3]]  # 1행 1열이 시작.
data = [[3, 'D'], [15, 'L'], [17, 'D']] 

def solution():
    info = []
    board = [[0]*N for _ in range(N)]
    now = (0,0)
    board[now[0]][now[1]] = 1
    info.append((now[0], now[1]))
    length = 1

    heads = ['L','R','U','D']
    head = 'R'
    time = 0 

    while True:
        time += 1
        if head == 'R':
            now = (now[0], now[1]+1)
        if head == 'L':
            now = (now[0], now[1]-1)
        if head == 'U':
            now = (now[0]-1, now[0])
        if head == 'D':
            now = (now[0]+1, now[0])

        if now[0] < 0 or now[0] > N-1 or now[1] < 0 or now[1] > N-1 or board[now[0]][now[1]] == 1:
            break
        else:
            board[now[0]][now[1]] = 1
            info.append((now[0]), now[1])
            if apple:
                if [now[0]+1, now[1]+1] in apple:
                    length += 1
                    apple.remove((now[0],now[1]))

            if len(info) > length:
                i, j = info.pop(0)
                board[i][j] = 0


    return time


    