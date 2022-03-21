from collections import deque

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
visit = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx,ry = i,j
            
        elif graph[i][j] == 'B':
            bx,by = i,j

def move(x,y,dx,dy):
    cnt = 0
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O': # 벽에 닿을때까지 기울이므로 while문
        x += dx
        y += dy
        cnt += 1    
    return x,y,cnt
    
q = deque([(rx,ry,bx,by,1)])

def bfs():
    
    while q:
        rx,ry,bx,by,cnt = q.popleft()
        
        if cnt > 10:
            break
        
        for i in range(4):
            nrx,nry,rcnt = move(rx,ry,dx[i],dy[i]) # 이동할 좌표
            nbx,nby,bcnt = move(bx,by,dx[i],dy[i])
            
            if graph[nbx][nby] != 'O': # B가 이동한 좌표가 O가 아니면 진행
                
                if graph[nrx][nry] == 'O': # R이 O에 도달하면 종료
                    print(cnt)
                    return
                
                # 예외 - 벽앞에서 두 구슬은 겹칠 수 없으므로, 많이 이동한 것을 뒤로 한칸 빼줌
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                         
                # 경우의 수 체크
                if not visit[nrx][nry][nbx][nby]:
                    visit[nrx][nry][nbx][nby] = True
                    q.append((nrx,nry,nbx,nby,cnt+1))
    
    print(-1)

bfs()
            