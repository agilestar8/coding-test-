def solution(gems):
    answer = []
    # 투 포인터
    n = len(gems)
    gem_kind = len(set(gems))
    i,j = 0,0
    dic = {}
    
    min_len = n+1
    while j<n: 
        if gems[j] not in dic:
            dic[gems[j]] = 1
        else:
            dic[gems[j]] += 1
        j += 1
        
        if gem_kind == len(dic):
            while i<n:
                if dic[gems[i]] > 1:
                    dic[gems[i]] -= 1
                    i += 1
                    
                elif j-i < min_len: # 더 최소길이라면 
                    min_len = j-i
                    answer = [i+1,j]
                    break   # 종료
                
                else: # 한 보석이 1개밖에 없을 때(없애면 종류줄으므로) 
                    break   # 종료
                
    return answer