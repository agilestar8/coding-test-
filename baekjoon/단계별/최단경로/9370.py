import sys, heapq
input = sys.stdin.readline
# t = int(input())

n,m,t = map(int,input().split())
s,g,h = map(int,input().split())
graph = [[] for _ in range()]
inf = 1e9
distance = [inf]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0],cost))


dijkstra() 

for i in range(1, n+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])

            

            



