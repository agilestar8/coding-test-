import heapq,sys
input = sys.stdin.readline

# 벨만포드 알고리즘은, 다익스트라 알고리즘의 최적해를 '항상' 포함한다.
n,m = map(int,input().split())
inf = 1e9
distance = [inf]*(n+1)
distance[1] = 0
edges = []  # 모든 간선에 대한 정보

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))   # 간선 정보
    
def velmanford(s):
 
    for i in range(n): # 매 노드 마다
        for j in range(m): # 모든 간선 확인
            
            now = edges[j][0]   # 출발노드 번호
            next = edges[j][1]  # 도착노드 번호
            cost = edges[j][2]  # 비용

            # 현재 간선을 거쳐가는게 더 빠를 경우
            if distance[now] != inf and distance[next] > distance[now] + cost: 
                distance[next] = distance[now]+cost # 갱신
                
                # 갱신했을때 노드를 검사했는데, 마지막 노드라면, 한바퀴 넘게 돌았단 것
                if i == n-1: # 음수순환 존재 시, 종료
                    return True 
    
    return False



if velmanford(1): # 음수순환 사이클이 있으면
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i] != inf:
            print(distance[i])
        else:
            print(-1)
            

    