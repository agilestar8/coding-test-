import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([(start[0], start[1])])     # 시작점좌표(0,0)

    while q:
        x,y = q.popleft()   # 현재좌표
        if abs(x-dest[0])+abs(y-dest[1]) <= 1000:   # 도착지점까지 남은거리 1000이하면 ㄱㅊ
            print("happy")
            return
        
        # 거리가 1000넘게 남았으면
        for i in range(n):  # 편의점 수 만큼
            if not visit[i]:    # 아직 안 들린 편의점인데,
                # nx,ny = arr[i]  # 현재 편의점의 좌표
                if abs(x-arr[i][0])+abs(y-arr[i][1]) <= 1000: # 편의점과의 거리가 1000이하면(맥주충전가능)
                    q.append((arr[i][0],arr[i][1]))           # 다음좌표로 진행
                    visit[i] = 1                # 방문처리
                    
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
    
    


