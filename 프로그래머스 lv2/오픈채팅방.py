def solution(record):
    answer = []
    dic = {}
    
    for i in record:
        info = i.split() # 행동0, uid1, 닉네임2  
        a = info[0] 
        uid = info[1]
        if len(info) == 3:
            nick = info[2]

        if a == "Enter": # enter일때 uid에 따른 닉네임 업데이트
            dic[uid] = nick
        elif a == "Change": # change면 uid 업데이트
            dic[uid] = nick

            
    for i in record:
        info = i.split() # 행동0, uid1, 닉네임2  
        a = info[0] 
        uid = info[1]
        if len(info) == 3:
            nick = info[2]
        
        temp = ""
        if a == "Enter":
            temp += dic[uid]+"님이 들어왔습니다."
            answer.append(temp)
        elif a == "Leave":
            temp += dic[uid]+"님이 나갔습니다."
            answer.append(temp)
     
    return answer