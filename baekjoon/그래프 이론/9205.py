import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([(start[0], start[1])])     # 시작점좌표(0,0)

    while q:
        x,y = q.popleft()
        if abs(x-dest[0])+abs(y-dest[1]) <= 1000:   # 도착지점까지 남은거리 1000이하면 ㄱㅊ
            print("happy")
            return
        
        # 1000이상이면
        for i in range(n):
            if not visit[i]:
                nx,ny = arr[i]
                if abs(x-nx)+abs(y-ny) <= 1000:
                    q.append((nx,ny))
                    visit[i] = 1
    print("sad")
    return

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []    # 편의점 좌표
    start = list(map(int,input().split()))
    for i in range(n):
        x,y = map(int,input().split())
        arr.append((x,y))
    dest = list(map(int,input().split()))
    visit = [0 for _ in range(n+1)]

    bfs()
    
    


