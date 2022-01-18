import sys,heapq
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

v1,v2 = map(int,input().split())

inf = 1e9

def dijkstra(v):
    distance = [inf]*(n+1)
    distance[v] = 0
    q = []
    heapq.heappush(q, (0,v))
    
    while q:
        dist,now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))

    return distance
            
route = dijkstra(1)     # 1번노드에서부터 다른노드까지의 거리
route_v1 = dijkstra(v1) # v1에서부터 다른노드까지의 거리
route_v2 = dijkstra(v2) # v2에서부터 다른노드까지의 거리

# 1 -> v1 -> v2 -> n 
# 1 -> v2 -> v1 -> n
ans = min(route[v1] + route_v1[v2] + route_v2[n], route[v2] + route_v2[v1] + route_v1[n])
# 1) 1번부터v1 + v1부터v2 + v2부터 n
# 2) 1번부터v2 + v2부터v1 + v1부터 n
print(ans if ans < inf else -1)
        

