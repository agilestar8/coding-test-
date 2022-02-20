from collections import deque
    
def solution(places):
    
    def bfs(x,y,graph):
        visit = [[0]*5 for _ in range(5)]
        visit[x][y] = 0
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        q = deque([(x,y)])            

        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<5 and 0<=ny<5 and not visit[nx][ny] and graph[nx][ny] != 'X':
                    visit[nx][ny] = visit[x][y] + 1 # 탐색한 거리가 맨하탄거리!
                    q.append((nx,ny))

        return visit    # 탐색한 거리를 리턴

    answer = []
    n = 5
    for graph in places:
        plist = []
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'P':  # P의 위치들 기록
                    plist.append((i,j))                
    
        isTrue = True # 거리두기 만족 여부
        for i in range(len(plist)): # 하나의 P에 대해서
            if isTrue: 
                for j in range(i+1,len(plist)): # 나머지 P들의 맨하탄거리 구하기
                    x,y = plist[i]
                    x2,y2 = plist[j]
                    result = bfs(x,y,graph)
                    if 1<=result[x2][y2]<=2: # 나머지P들 중 하나라도 맨하탄 거리가 1이상 2이하면, (0은 완전 막혀서 못간것이므로 조건만족임)
                        isTrue = False
                        break
            else: # 하나라도 거리두기 불만족 시
                break 

        if isTrue:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer