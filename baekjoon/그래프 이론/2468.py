import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = 1 # 답은 1이상 100이하

# 최대 높이 구하기
max_height = 0
for i in graph:
    a = max(i)    
    max_height = max(max_height, a)
    
# 1.DFS로하기
def DFS(x,y,h):             
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n and not visit[nx][ny] and graph[nx][ny] > h  :
            visit[nx][ny] = True
            DFS(nx,ny,h)
   
# 2.BFS로 하기            
def BFS(x,y):
    q = deque([(x,y)])           
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n and not visit[nx][ny] and graph[nx][ny] > h :
                visit[nx][ny] = True
                q.append((nx,ny))


for h in range(1,max_height+1): # 1 ~ 최대높이
    safe_area = 0
    visit = [[False]*n for _ in range(n)]
        
    # DFS해서 안전영역갯수 세기
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visit[i][j]:    # 침수안된 곳은 DFS/BFS
                visit[i][j] = True 
                safe_area += 1
                # DFS(i,j,h)
                BFS(i,j)
                
    ans = max(safe_area, ans)
            
print(ans)
    

# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7