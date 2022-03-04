def solution(tickets):
    
    # 티켓 확인
    dic = {}
    for i in tickets:
        if i[0] not in dic:
            dic[i[0]] = [i[1]]
        else:
            dic[i[0]].append(i[1])

    # 티켓 알파벳순 정렬
    for k,v in dic.items():
        v.sort(reverse = True)
        dic[k] = v
    print(dic)
    
    # 방문시작
    answer = []  
    q = ["ICN"] # ICN에서 시작
    while q: 
        city = q[-1] 
        if city in dic and dic[city]: # 티켓이 있으면
            nxt = dic[city].pop()     # 티켓써서
            q.append(nxt)             # 다음 도시로

        else:                         # 티켓 없으면
            answer.append(q.pop())    # 경로에 추가
    
    print(answer) 
    return answer[::-1]