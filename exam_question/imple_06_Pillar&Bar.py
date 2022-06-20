# https://programmers.co.kr/learn/courses/30/lessons/60061

# 프로그램은 2차원 가상 벽면에 기둥과 보를 이용한 구조물을 설치할 수 있는데, 기둥과 보는 길이가 1인 선분으로 표현되며 다음과 같은 규칙을 가지고 있습니다.

# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
# 단, 바닥은 벽면의 맨 아래 지면을 말합니다.

# 2차원 벽면은 n x n 크기 정사각 격자 형태이며, 각 격자는 1 x 1 크기입니다. 맨 처음 벽면은 비어있는 상태입니다. 
# 기둥과 보는 격자선의 교차점에 걸치지 않고, 격자 칸의 각 변에 정확히 일치하도록 설치할 수 있습니다. 다음은 기둥과 보를 설치해 구조물을 만든 예시입니다.


# 1. 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 2. 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.


n = 5  #벽면의 크기
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],      # [가로좌표, 세로좌표, (0 기둥, 1 보), (0 삭제, 1 설치)]
               [5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]      # 기둥은 위쪽방향으로 설치, 보는 오른쪽 방향으로 설치

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:   # 설치된 것이 기둥인 경우
            # '바닥위' '보의 한쪽 끝부분위' '다른 기둥위'
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1:  # 설치된 것이 보인 경우
            # '한쪽 끝 부분이 기둥위' '양쪽 끝부분이 다른 보와 동시에 연결'
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff])   # 일단 제거
            if not possible(answer):       # 가능하지 않다면
                answer.append([x,y,stuff]) # 다시 설치

        elif operate == 1:  # 설치하는경우
            answer.append([x, y, stuff])     # 일단 설치
            if not possible(answer):         # 가능하지 않다면
                answer.remove([x, y, stuff]) # 다시 제거

    return sorted(answer)


print(solution(n, build_frame))