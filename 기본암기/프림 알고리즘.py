import sys,heapq
input = sys.stdin.readline

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
visit = [0]*(v+1)

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

# 프림알고리즘에서 최소가중치의 순서로 넣어기위해 heapq를 써야하므로
# 그래프에 넣을 때 (weight, node) 순서로 넣어야함

def prim(w,n):
    q = []
    heapq.heappush(q, (w,n))
    global weight_cunsum
    weight_cunsum = 0
    cnt = 0
     
    while q:        
        if v == cnt:
            break

        w,n = heapq.heappop(q)  # **최소가중치 순서로 탐색
                
        if not visit[n]:    # 방문안했으면
            visit[n] = 1    # 방문하고
            cnt += 1        # 간선 +1
            weight_cunsum += w        # MST의 가중치의 합
        
            for i in graph[n]:  # 주변노드 탐색
                heapq.heappush(q, i)
            
            
prim(0,1)   # 1번노드부터 시작, 가중치는 0
print(weight_cunsum)

