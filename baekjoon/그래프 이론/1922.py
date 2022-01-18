import sys,heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

def prim(w,v):
    q = []
    heapq.heappush(q, (w,v))    # 가중치,노드번호
    global mst  # 최소 가중치의 합
    mst = 0
    cnt = 0     # 그려나갈 간선 개수
    
    while q:
        if cnt == n:
            break
        
        w,v = heapq.heappop(q)  # 우선순위로 q에서 뺀
        if not visit[v]:    # 방문안한 노드에
            visit[v] = True # 방문
            cnt += 1        # 간선 추가
            mst += w        # 최소 가중치 추가
            
            for i in graph[v]:      # 인접노드들
                heapq.heappush(q,i) # heapq에 추가

prim(0,1)
print(mst)             
