import sys
input = sys.stdin.readline
inf = 1e9

n = int(input())
m = int(input())
graph = [[inf]*(n+1) for _ in range(n+1)]   # 0제외, 1 ~ N번노드까지

# 초기화
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0     # 자기자신에게는 못감

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c             # A-->B, 비용은 C


# 알고리즘 구현
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            

# 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == inf:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()
            