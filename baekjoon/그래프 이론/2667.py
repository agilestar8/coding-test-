import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input()) for _ in range(n)]
house_cnt = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def DFS(x,y):
    global count
    count += 1 
    graph[x][y] = 0 # 1지우면서 카운트하기
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n and graph[nx][ny] == '1':
            DFS(nx,ny)
            
            
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            count = 0 # count 초기화
            DFS(i,j) 
            house_cnt.append(count)
            
print(len(house_cnt))
for i in sorted(house_cnt):
    print(i)      

    


