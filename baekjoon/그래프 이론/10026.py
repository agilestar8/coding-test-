import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
graph = [list(input()) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt = 0
cnt2 = 0

def DFS(x,y):
    visit[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n and graph[nx][ny] == graph[x][y] and not visit[nx][ny]:
            visit[nx][ny] = True
            DFS(nx,ny)


visit = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            cnt += 1 
            DFS(i,j)
            

visit = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] = "G"

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            cnt2 += 1
            DFS(i,j)


print(cnt, cnt2)




            

            
            
            