import heapq,sys
input = sys.stdin.readline

v,e = map(int,input().split())
k = int(input())

inf = 1e9
distance = [inf]*(v+1) # K노드부터 1번~V번노드까지의 거리
distance[k] = 0        # 자기자신까지 거리는 0

# 인접리스트로 그래프 구성하기
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))  # a에서 b로 가는 비용은 c
                            # b(i[0] = 노드번호), c(i[1] = 노드까지의 거리)

# 다익스트라 최단거리 알고리즘
def dijkstra(k):
    q = []
    heapq.heappush(q,(0,k))
    
    while q:
        d,n = heapq.heappop(q)
        
        if d > distance[n]: # 현재거리 > 메모된 최단거리면,  최단거리 아니므로 무시
            continue
        
        for i in graph[n]:          
            cost = d + i[1]         
            if cost < distance[i[0]]:  
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
                
dijkstra(k)

print(distance)
for i in range(1,v+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])
                     
            
            
        



