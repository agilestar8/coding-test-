import sys, heapq
input = sys.stdin.readline

n = int(input())
# 인접 리스트 생성
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
start, end = map(int,input().split())

dist = [float('inf')]*(n+1)
visit = [False]*(n+1)
hq = [(0,start,[start])]

# 다익스트라 실행
while hq:
    curDist,curNode,path = heapq.heappop(hq)
    if visit[curNode]:
        continue
    if curNode == end:
        print(dist[end])
        print(len(path))
        print(*path)
        break
    
    visit[curNode] = True
    for toNode, toDist in graph[curNode]:
        d = curDist+toDist
        # if visit[toNode] or d >= dist[toNode]:
        #     continue
        dist[toNode] = d
        heapq.heappush(hq,(d,toNode,path+[toNode]))