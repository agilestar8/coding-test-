def solution(id_list, report, k):
    answer = []
    rcnt = {}
    s_list = []
    report_info = {}
    report = set(report) # 중복 신고 제거
    
    for i in report:
        a,b = i.split(" ")
        if a not in report_info:
            report_info[a] = [b]
        else:
            report_info[a].append(b)
        
        if b not in rcnt:
            rcnt[b] = 1
        else:
            rcnt[b] += 1
    
    # print(rcnt)
    for people,value in rcnt.items():
        if value >= k:
            s_list.append(people)
            
    # print(s_list)
    # print(report_info)
    
    for i in id_list:
        cnt = 0
        if i in report_info:
            rlist = report_info[i]
            for j in rlist:
                if j in s_list:
                    cnt += 1
        
        answer.append(cnt)        
    
    return answer