import sys
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

# 인접리스트
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(node):
    for i in graph[node]:   # 인접노드중에서
        if not visit[i]:    # 방문안했으면
            visit[i] = node # 방문하고, 현재노드가 그 노드의 부모다
            DFS(i)

def BFS(node):
    q = deque([node])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visit[i]:
                visit[i] = now # 부모노드는 현재노드
                q.append(i)
        
BFS(1)
# DFS(1)

for i in range(2,n+1):
    print(visit[i])
