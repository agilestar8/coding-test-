from collections import deque
import sys
input = sys.stdin.readline

m,n,h = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while q:
        x,y,z = q.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append((nx,ny,nz))
    
def check(graph):
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if graph[k][i][j] == 0:
                    return False
    return True

q = deque([])   # 익은 토마토들 위치파악 
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                q.append((i,j,k))

bfs()

ans = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            ans = max(ans, (graph[k][i][j]))

if check(graph):
    print(ans-1)
else:
    print(-1)
    




