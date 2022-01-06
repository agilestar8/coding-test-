import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph[0][0] = 1

def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()   # 기존 좌표에서
        for i in range(4):
            nx = x + dx[i]  # 탐색 이동
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == '1':
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1   # 이동거리 +1

bfs(0,0)
print(graph[n-1][m-1])

# 그래프 확인
# for i in range(n):
#     for j in range(m):
#         print(graph[i][j], end = " ")
#     print()

