from collections import deque
def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    visit = [0]*(n+1)
    
    def bfs(s):
        q = deque([s])
        visit[s] = 1
        
        while q:
            now = q.popleft()
            for i in graph[now]:
                if not visit[i]:
                    visit[i] = visit[now]+1
                    q.append(i)
    
    bfs(1)
    m = max(visit)
    answer = visit.count(m)
    
    return answer