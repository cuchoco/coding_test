# N 개 강의 1번~N번 번호가짐.
# 동시에 여러개 강의 들을수 있음. 
# N=3 일때 3번강의의 선수강의로 1번,2번이고 1,2번은 선수강의가 없다고하자.
# 1번: 30시간 2번:20시간 3번:40시간
# 최소시간: 1번:30  2번:20  3번:70번 (30+40)

# N개의 강의가 주어졌을때 수강에 걸리는 최소시간을 출력하라.

N = 5 
data = [
    [10,-1],        # 1번과목의 수강시간
    [10,1,-1],      # 2번과목의 수강시간, 선수과목
    [4,1,-1],       
    [4,3,1,-1],     # 4번과목의 수강시간, 선수과목, 선수과목
    [3,3,-1]
]


graph = [[] for i in range(N+1)]

indegree = [0] * (N+1)
time = [0] * (N+1)

for i in range(len(data)):
    inform = data[i]
    time[i+1] = inform[0]
    for j in inform[1:-1]:
        indegree[j] += 1
        graph[i+1].append(j)

def solution():
    


    
    return indegree

print(solution(data))