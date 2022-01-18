import sys,heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    
start,end = map(int,input().split())

inf = 1e9
distance = [inf]*(n+1)
distance[start] = 0

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost,i[1]))
    
dijkstra(start)
print(distance[end])
    
    
    
    
    
    
    
