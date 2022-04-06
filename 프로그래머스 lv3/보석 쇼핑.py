def solution(gems):
    answer = []
    # 투 포인터
    n = len(gems)
    gem_kind = len(set(gems))
    i,j = 0,0
    dic = {}
    
    min_len = 1e9
    while j<n: 
        if gems[j] not in dic:
            dic[gems[j]] = 1
        else:
            dic[gems[j]] += 1
        j += 1
        
        if gem_kind == len(dic): # 현재 정답이
            while i < n:
                if j-i < min_len: # 더 최소길이라면 
                    min_len = j-i
                    answer = [i+1,j] # 번호 저장
                    
                # 더 짧은 길이를 찾기위해 하나씩 줄여보기
                if dic[gems[i]] > 1:
                    dic[gems[i]] -= 1
                    i += 1          
                elif dic[gems[i]] == 1:
                    break

    return answer