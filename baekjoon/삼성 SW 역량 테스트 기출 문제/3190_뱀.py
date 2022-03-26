n = int(input())
k = int(input())
map_data = [[0]*(n+1) for _ in range(n+1)]
info = []
dx = [0,1,0,-1] # 동남서북 
dy = [1,0,-1,0] # 동쪽 = 열1칸 이동

for _ in range(k):
    x, y = map(int,input().split())
    map_data[x][y] = 1  # 사과는 1
    
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
        
def simulation():
    x,y = 1,1    
    map_data[x][y] = 2
    time = 0         # 시간 기록
    q = [(x,y)]      # 위치정보기록
    direction = 0    # 동쪽
    idx = 0
    
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx>=1 and nx<=n and ny >= 1 and ny <= n and map_data[nx][ny] != 2:
            if map_data[nx][ny] == 0:
                map_data[nx][ny] = 2
                q.append((nx,ny))
                px,py = q.pop(0)
                map_data[px][py] = 0
            if map_data[nx][ny] == 1:
                map_data[nx][ny] = 2
                q.append((nx,ny))            
        else:
            time += 1
            break
        
        time += 1
        x,y = nx,ny
        if idx < l and time == info[idx][0] :
            direction = turn(direction, info[idx][1])
            idx += 1
        
    return time
    
print(simulation())