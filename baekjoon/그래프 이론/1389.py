import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    q = deque([v])
    visit = [0 for _ in range(n+1)]
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visit[i]:
                visit[i] = visit[now] + 1
                q.append(i)
    visit[v] = 0
    return sum(visit)    
          
arr = []          
for i in range(1,n+1):
    arr.append(bfs(i))
     
print(arr.index(min(arr))+1)      


