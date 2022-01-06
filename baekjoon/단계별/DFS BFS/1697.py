from collections import deque

n,k = map(int,input().split())
visited = [0]*100001

def bfs():
    q = deque([(n,0)])  # 0초에 점n에 있다

    while q:
        v = q.popleft()
        num = v[0]  # 숫자
        time = v[1]  # 시간

        if num == k:    # 찾던 숫자면
            return time  # 종료

        if not visited[num]: # 해당 위치에 간적 없다면
            visited[num] = 1 # 해당 위치 방문

            if num-1 >= 0:
                q.append((num-1, time+1))
            if num+1 < 100001:
                q.append((num+1, time+1))
            if num*2 < 100001:
                q.append((num*2, time+1))

print(bfs())
