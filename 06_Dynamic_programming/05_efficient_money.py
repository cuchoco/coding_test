# N종류의 화폐, 최소한으로 이용해서 가치의 합이 M이 되도록하려한다.
# ex) 2원, 3원이 있을경우 15원을 만드는 최소개수는 3원 5개 이용.
# 불가능 할때는 -1 출력


def solution(N:list, M:int) -> int:
    
    # 오름차순 정렬
    N.sort()

    # d의 인덱스 금액, d의 값 최소개수 갱신.
    d = [10001] * (M+1)
    d[0] = 0 

    for i in range(len(N)): 
        for j in range(N[i], M+1):

            # N의 첫번째 화폐단위가 2인경우 d[2],d[4],d[6],d[8] -> 1,2,3,4 
            d[j] = min(d[j], d[j-N[i]]+1)

   

    return d[M] if d[M] != 10001 else -1


print(solution([2,3], 15))
print(solution([3,5,7], 4))