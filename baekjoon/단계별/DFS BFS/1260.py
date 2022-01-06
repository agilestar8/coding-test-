from collections import deque
import sys
input = sys.stdin.readline

n,m,start = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited_DFS = [False]*(n+1)
visited_BFS = [False]*(n+1)

# 인접행렬로 그래프 구성
for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def DFS(v):
    visited_DFS[v] = True
    print(v, end = " ")

    for i in range(1,n+1):
        if not visited_DFS[i] and graph[v][i] == 1: # 방문안했으면서, 연결되어있으면
            DFS(i)  # DFS로 탐색

DFS(start)
print()

def BFS(start):
    q = deque([start])
    visited_BFS[start] = True
    
    while q:
        v = q.popleft()
        print(v, end = " ")

        for i in range(1,n+1):
            if not visited_BFS[i] and graph[v][i] == 1: # 방문안했으면서, 연결되있으면
                q.append(i) # BFS로 탐색
                visited_BFS[i] = True

BFS(start)



