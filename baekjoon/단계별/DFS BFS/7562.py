from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    q = deque([(x,y)])
    graph[x][y] = 1

    while q:
        x,y = q.popleft()

        if target_x == x and target_y == y:
            print(graph[target_x][target_y]-1)

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < l and ny >= 0 and ny < l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))

dx = [-2, -1, 1, 2, 1, 2, -1, -2]
dy = [1, 2, 2, 1, -2, -1, -2, -1]

t = int(input())
for i in range(t):
    l = int(input())
    x,y = map(int,input().split())
    target_x, target_y = map(int,input().split())
    graph = [[0]*l for _ in range(l)]

    bfs(x,y)

# for i in range(l):
#     for j in range(l):
#         print(graph[i][j]-1, end = " ")
#     print()
