import sys,heapq
input = sys.stdin.readline

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
inf = 1e9
v1, v2 = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance = [inf]*(n+1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

    return distance
            
# 1 -> v1 -> v2 -> n 또는 1 -> v2 -> v1 -> n
root = dijkstra(1)        
v1_root = dijkstra(v1)
v2_root = dijkstra(v2)
answer = min(root[v1] + v1_root[v2] + v2_root[n], root[v2] + v2_root[v1] + v1_root[n])
print(answer if answer < inf else -1)