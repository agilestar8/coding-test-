import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000)

n = int(input())
p1,p2 = map(int,input().split())    # p1과 p2의 관계구하기
m = int(input())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)   # 촌수 세야하므로 0으로 초기화

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v):
    for i in graph[v]:
        if not visit[i]:
            visit[i] = visit[v] + 1
            dfs(i)

def bfs(v):
    q = deque([v])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visit[i]:
                visit[i] = visit[now] + 1
                q.append(i)
        
# dfs(p1)
bfs(p1)

if visit[p2] > 0:
    print(visit[p2])
else:
    print(-1)

