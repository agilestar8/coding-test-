from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q = deque([(x,y)])
    area = 1
    graph[x][y] = 0
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                area += 1
                q.append((nx,ny))
                        
    return area
        
max_area = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            max_area = max(bfs(i,j), max_area)
            cnt += 1
        
print(cnt, max_area)


