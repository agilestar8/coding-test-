import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # DFS의 회귀수 제한

def DFS(x,y):
    graph[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny] == 1:
            DFS(nx,ny)

dx = [1,0,-1,0]
dy = [0,1,0,-1]           

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                DFS(i,j)
                cnt += 1
            
    print(cnt)
        