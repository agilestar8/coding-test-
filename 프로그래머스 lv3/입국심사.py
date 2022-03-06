def solution(n, times):
    left = 1 # 가장 최소 시간
    right = max(times)*n # 가장 오래걸리는 심사관으로만 심사한 시간
    
    while left < right:
        people = 0 # 심사받을수있는 사람 수
        
        mid = (left+right)//2
        
        for i in times:
            people += mid//i # 중간값으로 심사가능한 사람 세기
        
        if people >= n:  # n명이상 심사가능한 경우
            right = mid  # 긴 심사관 줄여서 더 짧게 가능한지 확인
                
        else:            # n명심사 불가능하면
            left = mid+1 # 짧은 심사관 횟수 늘려서 가능하게
    
    return left