from collections import deque
import sys,heapq
input = sys.stdin.readline

n,m,k,start = map(int,input().split())
graph = [[] for _ in range(n+1)]
inf = 1e9
distance = [inf]*(n+1)
distance[start] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((1,b))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:    
            continue
        
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))
                
dijkstra(start)
        
for i in range(1,n+1):
    if k not in distance:
        print(-1)
        break
    
    if distance[i] == k:
        print(i)
    
    


