def solution(m, n, board):
    answer = 0
    
    # board를 list형식으로
    graph = []
    for i in board:
        graph.append(list(i))
    
    while True:
        # 사라질 2x2들의 좌표찾기
        slist = []
        for i in range(m-1):
            for j in range(n-1):
                # 비어있지않고, 2x2가 같으면
                if graph[i][j] == graph[i][j+1] == graph[i+1][j] == graph[i+1][j+1] != '0':
                    slist.append((i,j))
                    slist.append((i+1,j))
                    slist.append((i,j+1))
                    slist.append((i+1,j+1))

        print(slist)
        slist = set(slist) # 터트릴 좌표(중복제거)
        
        if len(slist) == 0: # 터트릴거 없으면
            break           # 종료
        
        answer += len(slist)

        for x,y in slist: # 터진곳에 0 부여
            graph[x][y] = '0'

        # 블록 내리기
        for _ in range(m): # 열의 원소수만큼(행 수)
            for i in range(1,m): # 1행 부터(0행은 0이어도 의미없으니까)
                for j in range(n):
                    if graph[i][j] == '0': # 위에 0이면, 아래랑 교체
                        graph[i][j],graph[i-1][j] = graph[i-1][j],graph[i][j]
                    
    return answer