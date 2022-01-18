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
fish = []
time = 0

# 상어,물고기들의 좌표 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:        # 상어
            sx,sy = i,j
            graph[i][j] = 0

        elif 0 < graph[i][j] <=6:   # 물고기
            fish_cnt +=1
            fish.append((i,j))


def bfs(x,y):
    q = deque([(x,y,0)])
    dist_list = []
    min_dist = 1e9
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True
    
    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                
                if graph[nx][ny] <= shark_size:         # 지나갈수 있으면
                    visited[nx][ny] = True              
                    
                    if 0 < graph[nx][ny] < shark_size:  # 상어가 크면
                        min_dist = dist
                        dist_list.append((dist+1,nx,ny))
                        
                    if dist+1 <= min_dist:              # 
                        q.append((nx,ny,dist+1))
    if dist_list:
        dist_list.sort()
        return dist_list[0]
    else:
        return False

while fish_cnt :    # 물고기있으면
    result = bfs(sx,sy)
    if not result:
        break
    
    sx,sy = result[1],result[2]
    time += result[0]

    eat_cnt+=1
    fish_cnt-=1
    if shark_size == eat_cnt:
        shark_size +=1
        eat_cnt =0
    graph[sx][sy] = 0
    
print(time)