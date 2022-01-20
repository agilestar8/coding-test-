import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# DP + DFS사용 

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)] # 0은 나올수있는값이므로, -1로 초기화
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    # 도착 지점에 도달하면 1(한 가지 경우의 수)를 리턴
    if x == 0 and y == 0:   
        return 1
    
    if dp[x][y] == -1:  # 방문안했으면
        dp[x][y] = 0    # 방문    
        for i in range(4):  
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n: 
                if graph[x][y] < graph[nx][ny]: # 주변이 더 크면
                    dp[x][y] += dfs(nx,ny)      # 갈수있는 곳에서 dfs (거슬러올라감)
    
    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴               
    return dp[x][y]

print(dfs(m-1,n-1)) # 도착지에서 거꾸로 dfs

    

