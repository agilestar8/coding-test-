import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque([start])  # 시작노드를 큐에 넣고 시작
    binary[start] = 1    # 방문처리
  
    while q:
        now = q.popleft()
        for i in graph[now]:  # 인접노드들 중에서
            if binary[i] == 0:   # 방문안했으면
                binary[i] = -binary[now]    # 연결된 노드들에 마이너스(반대색)로 방문처리
                q.append(i)
            else:   # 방문했었는데
                if binary[i] == binary[now]:    #  자신과 인접노드가 동일하면 이분 그래프가 아님, break
                    return False
    return True           

t = int(input())
for _ in range(t):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    binary = [0 for _ in range(v+1)]
    check = True

    # 인접리스트 방식
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)  # 양방향 연결 a <-> b
        graph[b].append(a)
        
    for i in range(1, v+1):
        if binary[i] == 0:
            if not bfs(i):
                check = False
                break

    print("YES" if check else "NO")


