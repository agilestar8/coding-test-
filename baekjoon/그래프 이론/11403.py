n = int(input()) # 정점의 개수
graph = [list(map(int,input().split())) for _ in range(n)] # 입력은 인접행렬 방식

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][k] ==1 and graph[k][j] == 1):
                graph[i][j] = 1
            
for i in range(n):
    for j in range(n):
        print(graph[i][j], end = " ")
    print()
            
# 3
# 0 1 0
# 0 0 1
# 1 0 0




