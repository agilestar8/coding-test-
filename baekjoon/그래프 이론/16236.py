from pickle import FALSE
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visit = [[0]*n for i in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]


def bfs(x,y):
    q = deque([(x,y)])
    time = 0
    shark_size = 2 
    
    while q:
        x,y = q.popleft() 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]            
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] < shark_size:      # 상어가 더 크면
                    graph[nx][ny] = 0               # 잡아먹고 
                    visit[nx][ny] = visit[x][y] + 1 # 거리 1증가
                    time += 1                       # 시간 1증가
                    q.append((nx,ny))               # 위치이동
            
                elif graph[nx][ny] == shark_size:   # 같으면
                    time += 1
                    
                elif graph[nx][ny] > shark_size:    # 물고기가 더 크면
                    time += 1
                    visit[nx][ny] = visit[x][y] + 1 # 거리만 1증가
                    
                
                
fish = False                    
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and graph[i][j] != 9:
            fish = True
            break


