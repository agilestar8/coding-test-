def solution(msg):
    answer = []
    
    # 사전 초기화
    dic = {}
    for i in range(26):
        dic[chr(65+i)] = i+1

    # LZW
    w = 0 # 시작문자
    c = 1 # 다음문자

    while True:
        if c == len(msg): # 마지막 문자면
            answer.append(dic[msg[w:c]]) # 정답에 출력하고 종료
            break

        if msg[w:c+1] not in dic: # w+c가 사전에 없으면
            dic[msg[w:c+1]] = len(dic) + 1 # 사전에 추가
            answer.append(dic[msg[w:c]]) # 출력
            w = c 
            
        c += 1

    return answer