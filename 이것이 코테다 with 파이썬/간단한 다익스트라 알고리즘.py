import sys
input = sys.stdin.readline
inf = int(1e9)

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

# 입력
n,m = map(int,input().split())
start = int(input())

# 초기화
visited = [False] * (n+1)
distance = [inf] * (n+1)

# 그래프 생성
graph = [[] for i in range(n+1)]
for _ in range(m): # 모든 간선에 대해
    a,b,c = map(int,input().split())
    # a노드에서 b노드로 가는 비용이 c
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = inf
    idx = 0
    for i in range(1,n+1): # 1번노드부터 마지막노드까지 돌면서
        if distance[i] < min_value and not visited[i]: # 거리가 무한이 아니고 방문 안했다면
            min_value = distance[i] # 최소거리 저장
            idx = i
    return idx

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]: # 시작노드와 연결된 주변 노드들 중에
        distance[j[0]] = j[1] # 그 노드들의 거리 j[1]를 distance에 메모

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1] # 여태까지의 거리 + 다음 노드의 거리를 저장
            # 현재 노들를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]: # 여태 기록한 최단거리와 현재 노드에서 계산한 최단거리 비교
                distance[j[0]] = cost # 만약 더 최적을 발견하면 교체

# 알고리즘 수행
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == inf:
        print("INFINITY")
    else:
        print(distance[i])
