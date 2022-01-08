import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(x,y):
    q = set([(x,y,graph[x][y])]) # x,y,알파벳이 담긴 set리스트
    cnt = 1
        
    while q:
        x,y,alpha = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<r and ny>=0 and ny<c and graph[nx][ny] not in alpha:
                    q.add((nx, ny, graph[nx][ny]+alpha )) # set에 알파벳을 추가하는데, 중복알파벳 일시 추가안돰
                    cnt = max(cnt, len(alpha)+1)
    
    print(cnt)

BFS(0,0)

    
