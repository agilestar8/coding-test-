n = int(input()) # 정점의 개수
graph = [list(map(int,input().split())) for _ in range(n)] # 입력은 인접행렬 방식

# 플루이드 와셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            
            # 바로 i -> j가 되거나, i -> k -> j가 가능하다면 
            # i -> j로가는 선이 존재한다는 것
            if graph[i][j] == 1 or (graph[i][k] ==1 and graph[k][j] == 1):                 
                graph[i][j] = 1
            
for i in range(n):
    for j in range(n):
        print(graph[i][j], end = " ")
    print()
   



