import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
visited = [False]*(n+1)
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

cnt = 0
def dfs(v):
    global cnt
    visited[v] = True

    for i in range(1,n+1):
        if not visited[i] and graph[v][i] == 1:
            cnt += 1
            dfs(i)

dfs(1)
print(cnt)


