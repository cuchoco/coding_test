from itertools import product

def knigt1(data:str) -> int:
    count = 0
    offset = 1
    _y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    x = int(data[1]) - offset 
    y = int(_y.index(data[0]))

    # 왼쪽 꼭지점 x,y 가 0,0 이라고 가정.
    move_type = ['h_v', 'v_h'] # horizontal, vertical

    for move in move_type:
        if move == "h_v":
            dx = [-2, 2]
            dy = [-1, 1]
            for nx, ny in product(dx, dy):
                new_x = x + nx
                new_y = y + ny
                if new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8:
                    count += 1
    
        elif move == "v_h":
            dx = [-1, 1]
            dy = [-2, 2]
            for nx, ny in product(dx, dy):
                new_x = x + nx
                new_y = y + ny
                if new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8:
                    count += 1

    return count

# ---------------------------------------
# solution

def knigt2(data):
    x = int(data[1])
    y = int(ord(data[0])) - int(ord('a')) + 1

    steps = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)] 
    count = 0

    for step in steps:
        next_x = x + step[0]
        next_y = y + step[1]

        if next_x >= 1 and next_y >=1 and next_x <= 8 and next_y <= 8:
            count += 1
    
    return count


print(knigt1('a1'))
print(knigt2('a1'))


