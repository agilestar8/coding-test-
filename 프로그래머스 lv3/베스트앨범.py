def solution(genres, plays):
    answer = []
    n = len(genres)
    dic = {}
    
    # 장르 별 (번호,재생수)
    for i in range(n):
        if genres[i] not in dic:
            dic[genres[i]] = [[i,plays[i]]]
        else:
            dic[genres[i]].append( [i,plays[i]] )
    print(dic)
    
    # 장르 별 총재생수
    dic2 = {}
    for i,j in zip(genres,plays):
        if i not in dic2:
            dic2[i] = j
        else:
            dic2[i] += j
    dic2 = sorted(dic2.items(), key = lambda x : -x[1]) # 큰 재생수로 정렬
    print(dic2)
    
    # 각 장르에 대해서 조건대로 2개씩 뽑아내기
    for i,j in dic2:
        cnt = 0
        arr = sorted(dic[i], key = lambda x : (-x[1],x[0]))
        for k in arr:
            answer.append(k[0])
            cnt += 1
            if cnt == 2:
                break
                
    return answer