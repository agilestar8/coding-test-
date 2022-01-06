import sys
input = sys.stdin.readline
from collections import deque
import copy

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
max_area = 0
        
def virus_BFS():    
    temp = copy.deepcopy(graph)     # 백트래킹용 그래프
    
    q = deque([])   
    # 바이러스들 위치파악
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i,j)) # 큐에 담음
            
    # BFS
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and temp[nx][ny] == 0: # 길 있으면
                temp[nx][ny] = 2    # 바이러스 전파
                q.append((nx,ny))
            
    global max_area    
    area = 0
    # 안전영역 갯수 세기
    for i in range(n):
        area += temp[i].count(0)

    # 최대값 저장
    max_area = max(max_area, area)


def wall(cnt):
    if cnt == 3:    # 벽 3개 세웠으면 BFS돌려서 안전영역 개수 세기
        virus_BFS()
        return 0    # 종료
    
    # 벽 세워보기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:    # 벽 없으면
                graph[i][j] = 1     # 세우기
                wall(cnt+1)         # cnt는 1증가
                graph[i][j] = 0     # 다른 경우의 수 탐색
    
wall(0)
print(max_area)

  

    
  