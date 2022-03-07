def solution(n, times):
    left = 1 # 가장 최소 시간
    right = max(times)*n # 가장 오래걸리는 심사관으로만 심사한 시간
    
    # 더 많은 인원을 심사할 수 있다면 현재 탐색한 시간보다 아래쪽에서 다시 찾고, 
    # 심사해야 하는 인원수보다 현재 심사 가능한 인원수가 더 작다면 위쪽에서 다시 찾는다.

    while left < right:
        people = 0 # 심사받을수있는 사람 수
        
        mid = (left+right)//2
        
        for i in times:
            people += mid//i # 중간값으로 심사가능한 사람 세기
        
        if people >= n:  # n명 이상 심사가능한 경우
            right = mid  # 심사시간 더 짧게 가능한지 확인
                
        else:            # n명 불가능하면
            left = mid+1 # 심사시간 늘리기
    
    return left