import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 인접행렬로 그래프 구성
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

v_dfs = [False]*(n+1)
cnt = 0

def DFS(v):
    v_dfs[v] = True    
    global cnt
    cnt += 1
    for i in range(1,n+1):
        if graph[v][i] == 1 and not v_dfs[i]:
            DFS(i)
            
DFS(1)
print(cnt-1)





