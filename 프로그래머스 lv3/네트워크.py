from collections import deque
def solution(n, computers):
    answer = 0

    graph = [[] for _ in range(n)]
    edge = []
    # 인접행렬에서 간선을 뽑아내서, 인접리스트로
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j] == 1:
                edge.append([i,j])  # 간선뽑아내기

    # 인접리스트
    for a,b in edge:
        graph[a].append(b)
                    
    visit = [0]*n
    
    def bfs(s):
        q = deque([s])
        visit[s] = 1
        while q:
            v = q.popleft()
            for i in graph[v]:
                if not visit[i]:
                    visit[i] = 1
                    q.append(i)

    cnt = 0                    
    for i in range(n):
        if not visit[i]:
            bfs(i)
            cnt += 1
                    
    return cnt