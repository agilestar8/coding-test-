import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

def BFS(start):
    visit = [False for _ in range(n+1)]
    q = deque([start])
    cnt = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visit[i]:
                visit[i] = True
                cnt += 1
                q.append(i)
    return cnt

ans = []
max_hacked = 0
for i in range(1,n+1):
    hacked = BFS(i)
    
    if hacked > max_hacked: # 최대값만 업데이트 후, 따로저장
        max_hacked = hacked
        
    ans.append([i,hacked])

for i,cnt in ans:      
    if cnt == max_hacked:
        print(i, end = " ")
    
    