from collections import deque
import sys
input = sys.stdin.readline

# 특정 노드에서 다른 노드들까지의 거리 계산하기 - BFS,다익스트라

n, m, k, x = map(int,input().split())   # 도시 수, 간선 수, 최단거리k일때, x에서 출발
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
distance[x] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)  # a번노드에서 b번노드로 간선있음

q = deque([x])
while q:
    v = q.popleft()
    for i in graph[v]:
        # 방문 안했으면
        if distance[i] == -1:
            # 최단거리 갱신
            q.append(i)
            distance[i] = distance[v] + 1


for i in range(1,n+1):
    if distance[i] == k:
        print(i)

if k not in distance:
    print(-1)


# case1
# 4 4 1 1
# 1 2
# 1 3
# 2 3
# 2 4
# case2
# 4 3 2 1
# 1 2
# 1 3
# 1 4