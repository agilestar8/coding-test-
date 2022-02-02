import sys
input = sys.stdin.readline

r,c = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(r)]
visit = [[0]*c for _ in range(r)]
dx = [-1,0,1]   # 오른 위, 오른, 오른 아래 순서로 서치해서 끝에 닿으면, 경로 확정
dy = [1,1,1]

def dfs(x,y):    
    visit[x][y] = 1
    
    if y == c-1:    # 끝에 도달 시
        return True # DFS종료

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
            
        if 0<=nx<r and 0<=ny<c and graph[nx][ny] == "." and not visit[nx][ny]: # 다음칸이 빈칸이면
            visit[nx][ny] = 1   # 방문하고            
            if dfs(nx,ny):      # 끝까지 DFS가 가능하면, 계속
                return True     

    return False    # 끝까지 안된다면, DFS종료
         
for i in range(r):
    dfs(i,0)

answer = 0     
for i in visit:
    answer += i[-1]

print(answer)