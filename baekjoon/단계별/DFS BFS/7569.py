import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[] for i in range(h)]
q = deque([])

for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))

for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                q.append([x, y, z])

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while q:
        a,b,c = q.popleft()

        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]
            if nx >= 0 and nx < n and ny >=0 and ny < m and nz >= 0 and nz < h and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y]+1
                q.append([nx,ny,nz])

def check(graph):
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if graph[z][x][y] == 0:
                    return False
    return True

bfs()

answer = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            answer = max(answer,graph[z][x][y])

if check(graph):
    print(answer)
else:
    print(-1)





