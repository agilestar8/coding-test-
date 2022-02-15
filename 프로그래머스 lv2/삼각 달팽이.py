def solution(n):
    graph = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1
        
    for i in range(n): # 달팽이 채우기 n번
        for j in range(i, n): # 각 채우기 당 n번, n-1번, ... , 1번

            # 삼각형이므로, 3번하면 1회전임
            # 3으로 나눈 나머지 --> 0, 1, 2이면 각각 아래,오른,위 순서로 정의

            if i % 3 == 0: # 0이면 아래
                x += 1
                
            #right
            elif i % 3 == 1: # 1이면 오른쪽
                y += 1
                
            #up
            elif i % 3 == 2: # 2면 위방향
                x -= 1
                y -= 1
                
            graph[x][y] = num
            num += 1
            
    for i in graph:
        for j in i:
            if j != 0:
                answer.append(j)
    return(answer)

    for i in graph:
        print(i)
    