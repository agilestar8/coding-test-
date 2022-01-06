n,m = 4,4
x,y = 1,1
direction = 0

map = [[1,1,1,1],
       [1,0,0,1],
       [1,1,0,1],
       [1,1,1,1]]

# 첫 시작은 방문처리
map[x][y] = 1

dx = [-1,0,1,0] # 북 동 남 서
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
turn_time = 0

while 1:
    # 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 정면에 가보지 않은 칸이 존재하면 전진
    if map[nx][ny] == 0:
        map[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue

    else:
        turn_time += 1
        
    # 네 방향 모두 막힌 경우
    if turn_time == 4:
        # 후진할 좌표
        nx = x - dx[direction]
        ny = y - dx[direction]
        # 뒤로 갈 수 있다면 이동
        if map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)