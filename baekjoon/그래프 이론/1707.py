import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    q = deque([v])
    visit[v] = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visit[i]:            # 방문안했으면
                visit[i] = -visit[now]  # 방문해서 인접노드는 반대부호 표시
                q.append(i)
            
            elif visit[i] == visit[now]:# 방문했는데, 인접노드의 부호가 같으면
                return False            # 이분그래프 아님

    return True
    
t = int(input())
for _ in range(t):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visit = [0 for _ in range(v+1)]
    all_node_check = True
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,v+1):
        if visit[i] == 0:   # 방문안했으면
            if not bfs(i):  # 모든 노드 다 bfs돌려서 하나라도 이분그래프 아니면 NO
                all_node_check = False
                break
        
    # 모든 노드에서 다 이분그래프 특성나오면 YES
    print("YES" if all_node_check else "NO")
                
           
            
                
        

        
            
