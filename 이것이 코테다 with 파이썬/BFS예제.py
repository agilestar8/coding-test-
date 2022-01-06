from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])      # 큐 생성하고 원소는 1(start)로 시작
    visited[start] = True       # 방문 처리

    while queue:    # 큐가 있는 동안
        v = queue.popleft() # 하나 빼내고
        print(v, end = " ")

        for i in graph[v]:  # 1과 연결된 2 3 8 중에서
            if not visited[i]:      # 방문 안한거 있으면
                queue.append(i)     # 큐에 넣고
                visited[i] = True   # 방문 처리함 ex) 2 -> 3 -> 8 이런식

graph = [  # 인접 리스트
    [],          # 0번 노드는 아무것도 연결되어 있지 않음
    [2, 3, 8],   # 1번 노드는 2,3,8번 노드와 연결
    [1, 7],      # 2번 노드는 1,7번 노드와 연결
    [1, 4, 5],   # ...
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
    ]

visited = [False]*9
bfs(graph, 1, visited)