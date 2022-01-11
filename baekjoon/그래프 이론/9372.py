import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def bfs(v):
    q = deque([v])
    visit[v] = 1
    cnt = 0
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visit[i]:
                visit[i] = 1
                cnt += 1
                q.append(i)
    return cnt

for _ in range(t):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    print(bfs(1))    



            





