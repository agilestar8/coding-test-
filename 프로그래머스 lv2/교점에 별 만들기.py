def solution(line):
    star_list = []
    
    for i in range(len(line)): # 한 직선과
        for j in range(i+1,len(line)): # 나머지 직선들, 2개씩 비교        
            a, b, e = line[i] # ax + by +e의 계수
            c, d, f = line[j] # cx + dy +f의 계수
            
            # 두 직선에서 ad-bc가 0이 아니면 교점이 존재!
            if a*d-b*c !=0: 
                # 두 직선의 교점이 존재할 경우 교점의 좌표
                x = (b*f-e*d)/(a*d-b*c) 
                y = (e*c-a*f)/(a*d-b*c)
                # 두 좌표가 정수면
                if x.is_integer() and y.is_integer():
                    x,y = int(x),int(y)
                    # 교점 리스트에 없으면 추가
                    if (x,y) not in star_list: 
                        star_list.append((x,y))
                        
    x_min = min(star_list)[0] # 교점들 중 가장작은 x
    x_max = max(star_list)[0] # 교점들 중 가장 큰 x
    y_min = min(star_list,key = lambda x: x[1])[1] # 가장 작은 y
    y_max = max(star_list,key = lambda x: x[1])[1] # 가장 큰 y
    print(star_list)
    
    # 별을 그릴 좌표평면 크기 : x,y의 최소부터 최대까지+1
    star = [['.']*(abs(x_max-x_min)+1) for _ in range((abs(y_max-y_min)+1))]

    # 2차원 평면상의 좌표 --> 2차원 배열의 좌표로 찍어내려면
    # x, y = abs(y_max-b) , abs(x_min-a)의 공식으로 구할 수 있다.
    for x,y in star_list: # 교점을 평면에 찍기
        x,y = abs(y_max-y), abs(x_min-x) 
        star[x][y] = '*'

    # 출력형식에 맞게 재조절
    for i,v in enumerate(star):
        star[i] = ''.join(v)

    # for i in star:
    #        print(i)
    return star

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
solution(line)

