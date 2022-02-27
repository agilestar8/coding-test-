def solution(rows, columns, queries):
    answer = []
    n = rows
    m = columns
    
    # 행렬 구성
    graph = [[0 for _ in range(m)] for i in range(n)]
    f = 1
    for i in range(n):
        for j in range(m):
            graph[i][j] = f
            f += 1
    
    # 행렬 회전하기
    for x,y,x2,y2 in queries:
        x,y,x2,y2 = x-1,y-1,x2-1,y2-1
        
        temp = graph[x][y] # 왼쪽위 값 저장
        min_value = temp
        
        # 왼쪽부터
        for j in range(x,x2):
            graph[j][y] = graph[j+1][y]
            min_value = min(min_value, graph[j][y])
            
        # 아래
        for j in range(y,y2):
            graph[x2][j] = graph[x2][j+1]
            min_value = min(min_value, graph[x2][j])

        # 오른쪽
        for j in range(x2,x, -1):
            graph[j][y2] = graph[j-1][y2]
            min_value = min(min_value, graph[j][y2])      
            
        # 위
        for j in range(y2,y,-1):
            graph[x][j] = graph[x][j-1]
            min_value = min(min_value, graph[x][j])
            
        graph[x][y+1] = temp
        answer.append(min_value)  
    
    return answer