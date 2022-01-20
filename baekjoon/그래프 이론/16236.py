import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

shark_size = 2 
eat_cnt = 0
time = 0

# 상어,물고기들의 좌표 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:        # 상어
            sx,sy = i,j
            graph[i][j] = 0
            

def bfs(sx,sy):
    q = deque([(sx,sy)])                # 상어위치에서 시작
    visit = [[0]*n for _ in range(n)]   # 매bfs마다 visit 초기화
    visit[sx][sy] = 1                   # 시작위치 방문처리
    distance = [[0]*n for _ in range(n)]
    fish = []   # 먹을 물고기 담기
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 제일 가까운 물고기찾아서 잡아먹을준비(위치랑 거리계산)
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:   

                if graph[nx][ny] <= shark_size:  # 상어보다작은물고기면(빈칸도 포함),
                    distance[nx][ny] = distance[x][y] + 1
                    visit[nx][ny] = 1 
                    q.append((nx,ny))
                    
                if graph[nx][ny] < shark_size and graph[nx][ny] != 0:   # 물고기있고, 상어보다 작으면 
                                                                        # (빈칸아니어야 fish에 추가가능, 상어보다 작다고 추가하먼 x)
                    fish.append((nx,ny,distance[nx][ny]))               # 먹킷리스트에 추가
                    
    if fish:
        fish.sort(key = lambda x : (x[2],x[0],x[1]))  # 거리,x,y순 정렬
        return fish[0][0],fish[0][1],fish[0][2] # 가장 우선순위인(배열의 가장왼쪽) 물고기의 x,y,거리 return
    else:
        return -1,-1,-1
                    
    
while True:
        
    sx,sy,dist = bfs(sx,sy) # bfs로 우선순위물고기 좌표가져옴
    if sx == -1:
        break
    
    graph[sx][sy] = 0       # 그 좌표 물고기 잡아먹음
    eat_cnt += 1            # 먹은수 +1
    
    if eat_cnt == shark_size:
        eat_cnt = 0
        shark_size += 1
    
    time += dist

print(time)