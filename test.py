from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    visit = [[0] * n for i in range(n)]
    visit[i][j] = 1 # 상어위치는 방문표시
    eat = []
    dist = [[0] * n for i in range(n)]

    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:  # 다음좌표 방문안했었으면
                
                if s[nx][ny] <= s[i][j]:  # 물고기 있을땐 상어크기보다 작거나같거나, 물고기없고 빈칸이면
                    q.append([nx, ny])  # 다음좌표에서 bfs이어서
                    visit[nx][ny] = 1   # 방문처리
                    dist[nx][ny] = dist[x][y] + 1   # 거리 계산
                    
                if s[nx][ny] < s[i][j]:  # 물고기있는데, 상어보다 작으면
                    eat.append([nx, ny, dist[nx][ny]])      # 먹킷리스트에 (x,y,거리) 저장
                    
    if not eat: # 먹을 생선없으면 -1
        return -1, -1, -1
    
    # bfs로 각각 생선들거리 다 계산한 후, (거리,x,y) 순서로 정렬
    eat.sort(key = lambda x : (x[2], x[0], x[1]))
    return eat[0][0], eat[0][1], eat[0][2]  # 가장가까운 물고기의 (x,y,거리)를 return

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
s = []
for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(n):
        if a[j] == 9:       # 상어면,
            s[i][j] = 2     # 상어크기 입력
            start = [i, j]  # 상어 좌표 저장

exp = 0
cnt = 0

while True:
    i, j = start[0], start[1]   # 상어의 x,y 좌표로
    ex, ey, dist = bfs(i, j)    # bfs해서 우선순위 물고기 구하기
    if ex == -1:                # 물고기 다먹어서 없으면 종료
        break
    
    s[ex][ey] = s[i][j]         # 상어(크기 2로 표시)는 잡아먹은 물고기 위치로 이동
    s[i][j] = 0                 # 기존상어 위치는 0 표시
    start = [ex, ey]            # 상어 위치좌표 업데이트
    exp += 1                    # 한마리먹어서 경험치+1
    
    if exp == s[ex][ey]:        # 경험치랑 사이즈랑 같으면 
        exp = 0                 # 경험치 초기화
        s[ex][ey] += 1          # 크기 +1

    cnt += dist                 # 정답에 방금 물고기먹은 거리 추가
print(cnt)