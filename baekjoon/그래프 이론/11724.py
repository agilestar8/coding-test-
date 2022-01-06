import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n,m = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited = [False]*(n+1)
cnt = 0

def DFS(v):
    visited[v] = True
    for i in range(1,n+1):
        if graph[v][i] == 1 and not visited[i]:
            DFS(i)
    
for i in range(1,n+1):
    if not visited[i]:
        cnt += 1
        DFS(i)

print(cnt)
    
# BFS로 풀기  
# import sys
# input = sys.stdin.readline
# from collections import deque

# n,m = map(int,input().split())
# graph = [[0]*(n+1) for _ in range(n+1)]

# for i in range(m):
#     a,b = map(int,input().split())
#     graph[a][b] = graph[b][a] = 1

# visited = [False]*(n+1)
# cnt = 0

# def BFS(v):
#     q = deque([v])
#     visited[v] = True
#     while q:
#         now = q.popleft()
#         for i in range(1,n+1):
#             if graph[now][i] == 1 and not visited[i]:
#                 q.append(i)
#                 visited[i] = True
        

# for i in range(1,n+1):
#     if not visited[i]:
#         cnt += 1
#         BFS(i)

# print(cnt)
    