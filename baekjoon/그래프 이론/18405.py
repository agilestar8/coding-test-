from collections import deque

n, k = map(int,input().split())
data = []
graph = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j))

data.sort()

ts,tx,ty = map(int,input().split())

q = deque(data)
while q:
    virus,s,x,y = q.popleft()
    if s == ts:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus,s+1,nx,ny))

print(graph[tx-1][ty-1])
