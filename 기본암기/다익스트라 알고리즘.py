import sys,heapq
input = sys.stdin.readline
# 백준 1753 최단경로 출력하기
inf = 1e9

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
start = int(input())
distance = [inf]*(v+1)  # 시작노드에서 1번노드 ~ v번 노드까지의 거리, 기록용
distance[start] = 0     # 자기자신에게의 거리는 0

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))  # a에서 b로 가는 비용은 c
                            # i[0] = 노드번호, i[1] = 노드까지의 거리

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # q에 (거리,노드)를 저장

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:    # 현재노드의 인접노드들에 대해서
            cost = dist + i[1]  # 현재노드에서 계산한 인접노드 i까지의 총 비용
            if cost < distance[i[0]]:   # 기록된 i까지 총 비용(distance)과 현재 노드에서 계산한 i까지 총 비용(cost) 비교
                distance[i[0]] = cost   # 더 비용(cost)이 적으면 업데이트
                heapq.heappush(q, (cost, i[0]))

dijkstra(start) # start노드부터에서 부터의 최단거리 계산 시작

for i in range(1,v+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])
