import heapq

def dijkstra(graph, distance):    
    q = []
    heapq.heappush(q, (0,1))    # 시작노드하는 노드
    while q:
        dist,now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue            
            
        for i in graph[now]:    
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost,i[1])) 

def solution(N, road, K):
    inf = 1e9
    distance = [inf]*(N+1)
    distance[1] = 0 # 자기자신에게는 0
    graph = [[] for _ in range(N+1)]
    for a,b,c in road:        
        graph[a].append((c,b))
        graph[b].append((c,a))
        
    dijkstra(graph, distance)
    answer = 0
    for i in range(1,N+1):
        if distance[i] <= K:
            answer += 1
               
    return answer