import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visit = [[0]*n for i in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

shark_size = 2 
eat_cnt = 0
fish_cnt = 0
fish_pos = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            q.
           
for i in range(n):
    for j in range(n):
        if 0 < graph[i][j] <=6:     # 물고기가 있으면
            fish_cnt +=1            # cnt +1
            fish_pos.append((i,j))  # 위치 기록
            
        elif graph[i][j] == 9:      # 상어의
            shark_x, shark_y = i,j  # 위치 기록
            graph[shark_x][shark_y]=0   # 잠시 비어놓음


def bfs(x,y):
    q = deque([(x,y,0)])
    visit[x][y] = 1
    arr = []
    min_dist = 1e9
    

    while q:
        x,y,dist = q.popleft() 
                
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]            
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                if graph[nx][ny] <= shark_size:   # 물고기가 상어보다 작으면
                    visit[nx][ny] = 1           # 이동
                    if 0<graph[nx][ny]<shark_size:  # 
                        min_dist = dist
                        arr.append((dist+1,nx,ny))
                    if  dist+1 <= min_dist:
                        q.append((nx,ny,dist+1))
                    
                    
        
