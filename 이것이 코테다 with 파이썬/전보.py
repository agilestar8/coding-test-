import heapq
import sys

inpurt = sys.stdin.readline
n, m, c = map(int,input().split())
inf = 1e9
graph = [[] for _ in range(n+1)]
distance = [inf]*(n+1)

for i in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(c):
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

cnt = 0
max_distance = 0
for d in distance:
    if d != inf: # 지나갈 수 있는 도시는
        cnt += 1 # +1
        max_distance = max(max_distance, d) # distance 중에서 제일 큰 것(오래걸리는 것) 고르기

print(cnt-1, max_distance)
# 3 2 1
# 1 2 4
# 1 3 2