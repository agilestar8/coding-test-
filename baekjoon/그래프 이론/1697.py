import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int,input().split())
line = [0]*100001   # 도착시간기록하는 arr
                    # index = 위치, value = 시간

def BFS(n): # n이 5일 시
    q = deque([n])
    
    while q:
        x = q.popleft()
        if x == k: # 조건 만족 시
            print(line[x]) # 거기까지 걸린 시간출력
            break
        
        for i in (x-1, x+1, x*2): # 5-1, 5+1, 5*2중에서
            if 0 <= i and i < 100001 and line[i] == 0: # 4,6,10에 아직 도착시간이 기록안됐으면 
                line[i] = line[x]+1 # 기존시간에서 +1초 해줌
                q.append(i) # 큐에도 넣어서 BFS계속
            
BFS(n)
