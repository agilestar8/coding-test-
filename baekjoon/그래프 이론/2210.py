import sys
input = sys.stdin.readline
from collections import deque

graph = [list(map(str,input().split())) for _ in range(5)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
arr = set()
# arr = []

def dfs(x,y,str):
    # if len(str) == 6:
    #     if str not in arr:
    # arr.append(str)
        # return
    if len(str) == 6:
        arr.add(str)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny, str+graph[nx][ny] )
                        
for i in range(5):
    for j in range(5):
        dfs(i,j,graph[i][j])

print(len(arr))
        

 
    