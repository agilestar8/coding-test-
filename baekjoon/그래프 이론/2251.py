import sys
input = sys.stdin.readline
from collections import deque

a,b,c = map(int,input().split())        # a,b,c의 용량
visit = [[0]*(b+1) for _ in range(a+1)] # a,b 물통에 담긴 현재 물의 양
ans = [0 for i in range(201)]

def bfs():
    q = deque([(0,0,c)])    # (0,0,c) -> 처음엔 c에만 가득 담겨있음
    
    while q:
            x, y, z = q.popleft()       # 현재 물의양
            
            if visit[x][y] == 1:
                continue

            visit[x][y] = 1
            
            # a가 비었으면, c는 차있음
            if x == 0: 
                ans[z] = 1
            
            # a -> b로 붓기
            if x+y > b:
                q.append([x+y-b,b,z])
            else:
                q.append([0,x+y,z])

            # a -> c
            if x+z > c:
                q.append([x+z-c,y,c])            
            else:
                q.append([0,y,x+z])
                
            # b -> a
            if x+y > a:
                q.append([a,x+y-a,z])
            else:
                q.append([x+y,0,z])
            # b-> c
            if y+z > c:
                q.append([x,y+z-c,c])
            else:
                q.append([x,0,y+z])
                
            # c -> a
            if x+z > a:
                q.append([a,y,x+z-a])
            else:
                q.append([x+z,y,0])
            
            # c -> b
            if y+z > b:
                q.append([x,b,y+z-b])
            else:
                q.append([x,y+z,0])

            
bfs()
for i in range(201):
    if ans[i]:
        print(i, end = " ")



