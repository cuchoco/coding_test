# up down left right 
# 공간의 크기 n x n , 계획서 L R U D

def coordinate(n:int, plans:list) -> tuple:
    x, y = 1, 1

    # L R U D 에 따른 x,y의 변화
    move_types = ['L', 'R', 'U', 'D']
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for plan in plans:
        idx = move_types.index(plan)
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx < 1 or ny <1 or nx > n or ny > n:
            continue
        x, y = nx, ny

    return (x, y)

print(coordinate(5, ['R','R','R','U','D','D']))

        

