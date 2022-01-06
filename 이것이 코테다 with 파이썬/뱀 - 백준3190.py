n = int(input())
k = int(input())
map_data = [[0]*(n+1) for _ in range(n+1)]
info = []
dx = [0,1,0,-1] # 동남서북
dy = [1,0,-1,0] # 동쪽 = 열1칸 이동

# 맵 정보
for _ in range(k):
    x, y = map(int,input().split())
    map_data[x][y] = 1  # 사과는 1

# 방향 회전 정보
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x),c))

def turn(direction, c):
    if c == "L":    # 왼쪽으로 회전
        direction = (direction-1)%4
    elif c == "D":  # 오른쪽으로 회전
        direction = (direction+1)%4
    return direction

def simulate():
    x, y = 1,1 # 시작 위치
    map_data[x][y] = 2  # 현재 위치는 2
    direction = 0       # 0은 동쪽, 이후 남1 서2 북3
    time = 0
    d_idx = 0
    q = [(x,y)]         # 뱀의 위치 정보 기록

    while True:
        # 이동할 좌표 nx,ny
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위 안에 있고, 몸통이 없는 위치일 때
        if nx>=1 and nx<=n and ny>=1 and ny<=n and map_data[nx][ny] != 2:

            # 이동할 좌표에 사과가 없다면 이동 후 꼬리 제거
            if map_data[nx][ny] == 0:
                map_data[nx][ny] = 2
                q.append((nx,ny))       # 위치정보 기록
                px, py = q.pop(0)       # 이전 위치 좌표 가져와서
                map_data[px][py] = 0    # 꼬리 제거

            # 사과가 있다면
            if map_data[nx][ny] == 1:
                map_data[nx][ny] = 2
                q.append((nx,ny))

        # 범위 밖(=부딪침)이거나 자신의 몸통이 있을 때
        else:
            time += 1
            break

        x, y = nx, ny
        time += 1

        if d_idx < l and time == info[d_idx][0]:    # 주어진 조건대로 회전해야하는 시간이면
            direction = turn(direction, info[d_idx][1])
            d_idx += 1

    return time

print(simulate())
                
                


# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D