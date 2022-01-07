import sys
from collections import deque
input = sys.stdin.readline

m,n,k = map(int,input().split())
graph = [[0]*n for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
area = [] # 넓이

# 도형 채우기
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):      # y2-y1, 세로길이들
        for j in range(x1,x2):  # x2-x1, 가로길이들
            graph[i][j] = 1     # 그래프에 채우기
            
def BFS(x,y):
    cnt = 1
    graph[x][y] = 1
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<m and ny>=0 and ny<n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                cnt += 1
                q.append((nx,ny))
    area.append(cnt)

for i in range(m):
    for j in range(n):            
        if graph[i][j] == 0:    
            BFS(i,j)
        
print(len(area))
for count in sorted(area):
    print(count, end = " ")

