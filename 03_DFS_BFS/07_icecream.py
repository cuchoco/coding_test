
def icecream(n,m, graph):
    # dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방
    def dfs(x,y):
        # 주어진 범위를 벗어나는 경우는 즉시 종료
        if x <= -1 or x >=n or y <= -1 or y>= m:
            return False
        
        #현재 노드를 방문하지 않았다면
        if graph[x][y] == 0:
            # 해당 노드 방문처리
            graph[x][y] = 1
            # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True
        return False

    count = 0

    for i in range(n):
        for j in range(m):
            #현재 위치에서 dfs 수행
            if dfs(i, j) == True:
                count += 1
    
    return count


n = 3
m = 3
graph = [
    [0,0,1],
    [0,1,0],
    [1,0,1]
]

print("icecream: ", icecream(n,m,graph))