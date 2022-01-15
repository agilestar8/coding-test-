import sys
from collections import deque
input = sys.stdin.readline

# 위상정렬 알고리즘
# 위상정렬의 과정은 다음과 같다.

# 1.진입차수가 0인 정점을 큐에 삽입
# 2.큐에서 원소를 꺼내 해당 원소와 연결된 간선을 모두 제거
# 3.제거한 후에 진입차수가 0인 정점을 큐에 삽입
# 4.이후 2~3의 과정을 반복

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
inDegree = [0]*(n+1)   # 1번부터 n번까지 진입차수
q = deque([])
ans = []

# 인접리스트로 그래프 구성
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)  # a에서 b로 가는 간선있음
    inDegree[b] += 1    # b의 진입차수 +1 (순서뒤로)

# 위상정렬
def topological_sorting():

    for i in range(1,n+1):      # 진입차수 검사
        if inDegree[i] == 0:    # 진입차수가 0이면
            q.append(i)         # 앞 순서로
        
    while q:
        v = q.popleft()
        ans.append(v)           # 진입차수0이므로 먼저 나옴
        
        for i in graph[v]:      # 나온 노드의 인접노드들의
            inDegree[i] -= 1    # 간선을 제거(진입차수 감소)

            if inDegree[i] == 0:# 진입차수가 0이면 
                q.append(i)     # 큐에 추가

topological_sorting()
print(*ans)    
