import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)] # n x m 그래프
dx = [1,-1,0,0] # 동,서,남,북으로 1칸 이동
dy = [0,0,1,-1] 
graph[0][0] = 1 # 시작점

def BFS(x,y):
    q = deque([(x,y)]) # 시작좌표 받아서
    while q:
        x,y = q.popleft()
        for i in range(4): # 4방향으로 이동가능
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 이동한 좌표가 그래프 내에 있고, 이동할 수 있는 칸이면
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == '1':
                q.append((nx,ny)) # 이동하고 BFS탐색 이어서하기
                graph[nx][ny] = graph[x][y] + 1 # 이동한거리 +1 기록하기
                
BFS(0,0) # 0,0에서 시작
print(graph[n-1][m-1])            

for i in range(n):
    for j in range(m):
        print(graph[i][j], end = " ")
    print()

# 4 6
# 101111
# 101010
# 101011
# 111011