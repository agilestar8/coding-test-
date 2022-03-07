def solution(routes):
    answer = 0    
    routes.sort(key = lambda x : x[1]) # 나간 순서로 정렬
    last_camera = -30001    # 마지막 카메라 위치
    
    for i,j in routes: # i~j사이에 카메라가 있어야 함
        
        if last_camera < i: # 카메라위치가 i보다 왼쪽이면
            answer += 1     # 해당 차를 위해 카메라 추가 설치
            last_camera = j # 카메라 위치 j로 갱신 
        
    return answer