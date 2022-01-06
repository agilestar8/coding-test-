import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10000

dx = [1,0,-1,0,1,-1,1,-1]
dy = [0,1,0,-1,1,-1,-1,1]

def DFS(x,y):    
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<h and ny>=0 and ny<w and graph[nx][ny] == 1:
            graph[nx][ny] = 0
            DFS(nx,ny)
            
while True:
    cnt = 0
    w,h = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                cnt += 1
                DFS(i,j)
        
    if w == 0 and h == 0:
        break
    print(cnt)



