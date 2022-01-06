import sys
input = sys.stdin.readline

def bellmanFord():
    global ispossible

    for repeat in range(n):     # 반복회수는 노드의 수 만큼

        for i in range(1,n+1):  # 1번노드부터 n번 노드까지
            for neighbor, dist in graph[i]:   # 인접노드의 거리
                if distance[i] != inf and distance[neighbor] > distance[i] + dist:
                    distance[neighbor] = distance[i] + dist  # 최단 거리 갱신
                    if repeat == n-1:
                        ispossible = False

inf = 1e9
n,m = map(int,input().split())
distance = [inf]*(n+1)
distance[1] = 0

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

ispossible = True

bellmanFord()

if not ispossible:
    print(-1)
else:
    for d in distance[2:]:
        print(d if d != inf else -1)



