import heapq
import sys

input = sys.stdin.readline
n,e = map(int,input().split())
start = int(input())

inf = 1e9
distance = [inf] * (n+1)

graph = [[] for i in range(n+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))      # a노드에서 b노드로 가는 가중치는 c

def dijkstra(start):
    # 큐 생성
    queue = []
    
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:    # 큐에 내용물이 있는 한
        dist, now = heapq.heappop(queue)  # 최단 거리인 노드에 대한 정보(거리,노드번호)빼내기
        if distance[now] < dist:    # 처리된 적 있는 노드면 무시
            continue

        for i in graph[now]:
            cost = dist + i[1]  # cost는 기록된 최단거리 + 다음노드 거리
            if cost < distance[i[0]]:
                distance[i[0]] = cost   # 최단거리 업데이트
                heapq.heappush(queue, (cost, i[0]))  # 업데이트 내용 큐에 넣음, 이때 cost기준 가장 작은 값이 맨위로 위치된다

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])

# 입력 예시
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
