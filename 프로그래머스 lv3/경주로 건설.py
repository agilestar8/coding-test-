from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    dx = [1,-1,0,0] 
    dy = [0,0,1,-1]
    visit = [[0]*n for _ in range(n)]
    
    def bfs(x,y,direct,cost):
        q = deque([(x,y,direct,cost)])
        visit[0][0] = 0
            
        while q:
            x,y,direct,cost = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<n and 0<=ny<n and board[nx][ny] != 1: # 벽이 아니면 진행
                    if nx == 0 and ny == 0:
                        continue
                        
                    if direct == -1: 
                        ncost = cost+100
                    elif direct == i:
                        ncost = cost+100
                    else:
                        ncost = cost+600
                    
                    if not visit[nx][ny]: # 첫 방문
                        visit[nx][ny] = ncost
                        q.append((nx,ny,i,ncost))
                    else:   # 다른 루트와 겹치면
                        if visit[nx][ny] >= ncost:
                            visit[nx][ny] = ncost
                            q.append((nx,ny,i,ncost))
                    
                                
        return visit[-1][-1]        
                    
    answer = bfs(0,0,-1,0)
    
    return answer