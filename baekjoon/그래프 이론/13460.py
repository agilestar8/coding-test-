import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [list(map(str,input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

red = []
blue = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx,ry = i,j
        elif graph[i][j] == 'B':
            bx,by = i,j
        

   
        
#  '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 
# 'O'는 구멍의 위치를 의미한다. 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.

# 입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 
# 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.
# 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 
# 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.






