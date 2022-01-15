from collections import deque
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

graph = [[0]*m for _ in range(n)]
for _ in range(k):
    r,c = map(int,input().split())
    graph[r-1][c-1] = 1
    
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q = deque([(x,y)])
    area = 0
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                area += 1
                q.append((nx,ny))
                graph[nx][ny] = 0
                
    return area

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans = max(ans, bfs(i,j))
                
print(ans)




