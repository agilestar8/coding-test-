import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

inf = 1e9
graph = [[inf]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0
            
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b], c)   # 걸리는 비용 중 최소만 저장
    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])   # 거쳐가는거랑 바로가는 것 중 최소값을 저장
            
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == inf:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()


