import sys
input = sys.stdin.readline

# 플루이드 와셜 알고리즘 : 모든 점에서 다른 모든 점까지의 최단거리 구함
n,m = map(int,input().split())
inf = 1e9
graph = [[inf]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0
            
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
                graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])
 
ans = 1e9   
for i in range(1,n+1):
    sum = 0
    for j in range(1,n+1):
        sum += graph[i][j]
    
    if ans > sum:
        ans = sum
        idx = i
        
print(idx)
        
    
    