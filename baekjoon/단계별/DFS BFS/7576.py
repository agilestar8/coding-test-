import sys
from collections import deque

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
q = deque([])    # 익은 토마토의 위치 파악
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def check(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return False
    return True

def bfs():
    # q의 초기값들은 맨 처음의 익은 토마토들의 위치
    while q:
        x,y = q.popleft()   # 익은 토마토들 fifo로 탐색

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0: # 주변 토마토가 안 익었으면
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))   # 익힌 후 queue에 넣어 다음에 bfs이어서 함
                
bfs()   # bfs 탐색 시작

answer = 0
for i in range(n):
    for j in range(m):
        # print(graph[i][j], end = " ")
        answer = max(answer,graph[i][j])
    # print()

if check(graph):
    print(answer-1)
else:
    print(-1)




    


            



