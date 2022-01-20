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

def dijkstra(start,end):
    q = []
    heapq.heappush(q, (0, start, [start]))  # (가중치,시작노드,[시작경로]), 큐에 경로담는 리스트 추가
    
    while q:
        dist, now, path = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
                
        if now == end:  # 지정된 노드에 도달하면 종료
            print(distance[end])
            print(len(path))
            print(*path)
            break 
                        
        for d, next_node in graph[now]:
            cost = dist + d
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node, path+[next_node]))
    
dijkstra(start,end)        


