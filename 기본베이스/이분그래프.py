from collections import deque

# 이분 그래프 복습
t = int(input())
for i in range(t):

    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    binary = [0 for _ in range(v + 1)]
    check = True

    # 인접리스트 그래프
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start):
        q = deque([start])
        binary[start] = 1   # 1번노드의 초기값 1

        while q:
            now = q.popleft()
            for i in graph[now]:    # 인접노드들 중에서
                if binary[i] == 0:  # 방문안했으면
                    binary[i] = -binary[now]    # 인접노드의 대칭값 부여
                    q.append(i)
                else:
                    if binary[i] == binary[now]:    # 자신과 인접노드가 같으면 이분그래프가 아님 False
                        return False
        return True

    for i in range(1, v+1):
        if binary[i] == 0:
            if not bfs(i):
                check = False
                break

    print("YES" if check else "NO")




