import sys,heapq
input = sys.stdin.readline

# 최소 신장 트리(Minimum Spannig Tree)는 최소한의 비용으로 모든 간선을 연결한 트리를 의미한다.
# 최소 신장 트리를 만드는 알고리즘으로 프림 알고리즘, 그리고 크루스칼 알고리즘이 있다.

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
visit = [False]*(v+1)

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])


def prim(weight,node):
    q = []
    heapq.heappush(q, [weight,node])
    global ans
    ans = 0 # 가중치 합
    cnt = 0 # 간선의 개수
    while q:
        if cnt == v:
            break
        
        weight, node = heapq.heappop(q)
        if not visit[node]:
            visit[node] = True
            cnt += 1
            ans += weight

            for i in graph[node]:
                heapq.heappush(q, i)

prim(0,1)        
print(ans)


