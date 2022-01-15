import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())

visit = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(start):
    q = deque([start])
    visit[start] = 1

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visit[i]:
                visit[i] = visit[v] + 1
                q.append(i)
    
bfs(1)
arr = []
for i in range(2,n+1):
    if 2 <= visit[i] <= 3:
        arr.append(i)
    
print(len(arr))    