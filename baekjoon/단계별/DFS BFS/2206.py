import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]
visit = [[[0] * 2 for i in range(m)] for i in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque([(0, 0, 1)])  # 시작지점 : 0,0 / 벽 카운트 : 1
visit[0][0][1] = 1

def bfs():    
    while q:
        x, y, w = q.popleft()
        
        if x == n-1 and y == m-1:   # 맨 끝에 도달 시
            return visit[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and w == 1: # 다음 칸이 벽에 막혀있고, 벽 카운트가 아직 있으면
                    visit[nx][ny][0] = visit[x][y][1] + 1  # 벽 카운트 0인 곳에서 진행(벽 부심)
                    q.append([nx, ny, 0]) # 벽 카운트 내린 상태로 큐에 삽입하여 진행

                elif graph[nx][ny] == 0 and visit[nx][ny][w] == 0:  # 길이 원래 있고, 다음칸에 갈 수 있으면
                    visit[nx][ny][w] = visit[x][y][w] + 1 # 진행
                    q.append([nx, ny, w]) # 벽 카운트 유지
    
    return -1

print(bfs())
