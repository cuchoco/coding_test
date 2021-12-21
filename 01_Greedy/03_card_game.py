# N x M 숫자카드 가장 높은 숫자가 쓰인 카드 한장 뽑기.
# 행을 선택하면 그 행에서 가장 낮은 숫자를 선택하게됨. 
import numpy as np

def game(n:int, m:int, data:np.array) -> int:
    
    max = 0 

    for row in data:
        min = row.min()
        if min > max:
            max = min
    
    return max

print(game(3,4, data = np.array([[7,3,1,8],[3,3,3,4],[5,8,6,7]]))) # 7