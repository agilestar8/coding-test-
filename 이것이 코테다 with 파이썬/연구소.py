n, m = map(int,input().split())
data = []
temp = [[0] * m for _ in range(n)]  # 벽을 설치한 뒤의 리스트

for _ in range(n):
    data.append(list(map(int,input().split())))
# 0빈칸, 1벽, 2바이러스

dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

result = 0

def virus(x,y):
    for i in range(4):  # 4방향으로 퍼짐
        nx = x + dx[i]
        ny = y + dy[i]
        # 상하좌우 뚫려서 바이러스가 갈수 있는 경우
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny] == 0:   # 빈 공간이면
                temp[nx][ny] = 2    # 바이러스 배치
                virus(nx,ny)        # 재귀로 퍼짐

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(cnt):
    global result

    # 벽3개 설치된 경우
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        # 바이러스 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)

        # 안전 영역 최대값 계산하고 탈출
        result = max(result,get_score())
        return True

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:     # 빈칸에
                data[i][j] = 1      # 벽 세우기
                cnt += 1

                dfs(cnt)
                data[i][j] = 0
                cnt -= 1

dfs(0)
print(result)

# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2