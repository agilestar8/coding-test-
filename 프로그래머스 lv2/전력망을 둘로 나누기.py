from collections import deque

# 간선 하나씩 빼보면서, BFS해보기

def solution(n, wires):
    def bfs(start,visit):
        q = deque([start])
        visit[start] = 1
        cnt = 1
        while q:
            v = q.popleft()
            for i in graph[v]:
                if not visit[i]:
                    visit[i] = 1
                    q.append(i)
                    cnt += 1
        return cnt

    graph = [[] for _ in range(n+1)]
    m = len(wires)

    for i in range(m):
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])

    min_cnt = 1e9
    for a,b in wires:   # a->b로 가는 간선
        visit = [0]*(n+1)
        visit[b] = 1    # b를 방문처리해놔서 a->b로 가지않음 (간선 무시)
        one = bfs(a,visit) # bfs해서 노드 세기
        two = n-one
        min_cnt = min(min_cnt, abs(one-two))

    return (min_cnt)


                





