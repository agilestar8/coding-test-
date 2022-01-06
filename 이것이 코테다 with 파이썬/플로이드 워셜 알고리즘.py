inf = int(1e9)
n = int(input())
m = int(input())

graph = [[inf] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용은 c
    a, b, c = map(int, input().split())
    # graph[a][b] = c
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            # a->b로 가는 비용과
            # a->k->b k를 경유한 후 가는 것의 비용 중 작은 것을 선택

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == inf:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()

# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2