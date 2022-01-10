import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]
visit = [[[0] * 2 for i in range(m)] for i in range(n)] # 3차원배열, 기존그래프 + 벽부수기 여부
dx = [1,0,-1,0]
dy = [0,1,0,-1]

q = deque([(0, 0, 1)])  # 시작지점 : 0,0 / 벽 부술 수 있는 횟수 : 1
visit[0][0][1] = 1

def bfs():
    while q:
        x,y,w = q.popleft()
        
        if x == n-1 and y == m-1:   # 맨끝에 도달 시
            return visit[x][y][w]   # 출력(최단거리)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                # 벽으로 막혀있지만, 1회 부술수 있으면
                if graph[nx][ny] == 1 and w == 1:   
                    visit[nx][ny][0] = visit[x][y][1] + 1   # 부수고 진행, 거리 1 증가
                    q.append((nx,ny,w-1)) # 다음으로 진행하지만, 이젠 벽 못부심 (nx,ny,0)
                
                # 벽 이미 한번 부셨으면 정상진행
                elif graph[nx][ny] == 0 and visit[nx][ny][w] == 0: 
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    q.append((nx,ny,w))
     
    return -1

print(bfs())
    
            
        
    