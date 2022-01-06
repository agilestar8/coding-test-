def dfs(graph, v, visited):
    # 현재 노드는 방문처리
    visited[v] = True
    print(v, end = " ")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:  # 1과 연결된 2 3 8 중에서
        if not visited[i]:  # 방문안한거 있으면
            dfs(graph, i, visited)  # Depth에서 dfs 다시 시작
                                    # ex) 2에 들어가서 방문체크, 2와 연결된 1,7중 방문안된 노드를 방문하는 재귀형태

graph = [       # 인접 리스트
    [],         # 0번 노드는 아무것도 연결되어 있지 않음
    [2,3,8],    # 1번 노드는 2,3,8번 노드와 연결
    [1,7],      # 2번 노드는 1,7번 노드와 연결
    [1,4,5],    # ...
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# visited = [False]*9
#
# dfs(graph, 1, visited)

print(graph)
