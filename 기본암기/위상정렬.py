import sys
input = sys.stdin.readline
from collections import deque

# 위상정렬은 deque 사용
# 진입차수 0부터 넣고, 인접노드들 차수 감소시키는 방식

n,m = map(int,input().split())      # 노드수, 간선수
graph = [[] for _ in range(n+1)]    # 인접리스트 그래프
indegree = [0]*(n+1)                # 진입차수, 초기값은 0

q = deque([])
ans = []

for _ in range(m):                  # 진입차수 정의
    a,b = map(int,input().split())  # 두 학생의 관계
    graph[a].append(b)              # a < b
    indegree[b] += 1                # b는 a의 다음순서 이므로 진입차수 +1


for i in range(1,n+1):      # 1번 노드부터
    if indegree[i] == 0:    # 진입차수가 0인 것들
        q.append(i)         # 큐에 담기


while q:    
    v = q.popleft() # 큐에서 진입차수0인 것들 
    ans.append(v)   # 정답에 넣기
        
    for i in graph[v]:         # 진입차수0의 인접노드들은
        indegree[i] -= 1       # 진입차수 1씩 감소
        if indegree[i] == 0:   # 감소시킨 진입차수가 0이면
            q.append(i)        # 큐에 넣기

print(*ans)
