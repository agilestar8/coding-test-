import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input()) for _ in range(n)]
house_num = []  # 단지 내 집 개수
cnt = 0
dx = [0,0,1,-1] # 동서남북
dy = [1,-1,0,0]

def dfs(x,y):
    global cnt
    graph[x][y] = 0
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == '1':
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            cnt = 0 # 각 단지 별로 cnt 초기화
            dfs(i,j)
            house_num.append(cnt)

print(len(house_num))
for i in sorted(house_num):
    print(i)
    
