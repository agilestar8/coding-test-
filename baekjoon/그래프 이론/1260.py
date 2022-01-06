from collections import deque
import sys
input = sys.stdin.readline

# 정점, 간선, 시작점
n,m,v = map(int,input().split())

# 점 개수에 따라 빈 그래프 생성
graph = [[0]*(n+1) for _ in range(n+1)]

# DFS,BFS의 방문여부 리스트
visit_dfs = [False] * (n+1)
visit_bfs = [False] * (n+1)

# 인접행렬로 그래프 구성, 인접리스트는 살짝 다름
for i in range(m): 
    a,b = map(int,input().split())  # 점 개수만큼 입력받기
    graph[a][b] = 1                 
    graph[b][a] = 1                 # : a와 b에는 1의 쌍방관계(간선)가 있다


# DFS 함수
def DFS(v): # v에서 시작
    visit_dfs[v] = True     # 시작점 v 방문처리
    print(v, end = " ")
    
    # 주변의 연결된 정점들 서치
    for i in range(1, n+1): # 1번점(낮은 번호)부터 시작
        if graph[v][i] == 1 and not visit_dfs[i]:   # 연결되있는데, 그 점을 아직 방문안했다면
            DFS(i)  # 연결된 다른 정점 뒤로하고, i를 시작점으로 삼고 DFS로 깊게 방문!
        
DFS(v)
print()

# BFS 함수
def BFS(start):
    q = deque([start]) # 큐 생성, 방문할 리스트
    visit_bfs[start] = True # 시작점 방문처리
    
    while q: # 방문할 리스트가 있으면
        v = q.popleft() 
        print(v, end = " ")
        
        for i in range(1,n+1):
            if graph[v][i] == 1 and not visit_bfs[i]: # 연결된 방문안한 정점이면
                q.append(i)         # 큐에 방문리스트순서에 추가(나중에 방문함)
                visit_bfs[i] = True # 같은 depth인 연결된 정점들은 (넓게)방문처리
        
BFS(v)



