import sys
input = sys.stdin.readline
from collections import deque

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

q = deque([])   # 익은 토마토들 위치파악 
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

def BFS(): # 여러 익은 토마토들이 동시에 BFS진행
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny] == 0:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
        
BFS()

# BFS한 이후, 익은 토마토가 없는 경우 체크
def check(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return False
    return True

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, (graph[i][j]))

if check(graph):
    print(ans-1)
else:
    print(-1)