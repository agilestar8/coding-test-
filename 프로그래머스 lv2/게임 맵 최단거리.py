from collections import deque

def solution(maps):    
    n = len(maps)
    m = len(maps[0])
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visit = [[0]*m for _ in range(n)]
    
    q = deque([(0,0)])
    visit[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx,ny))
                
    if visit[n-1][m-1] != 0:
        return visit[n-1][m-1]
    else:
        return -1