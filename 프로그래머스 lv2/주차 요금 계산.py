from math import ceil
def solution(fees, records):
    answer = []
    dic = {}
    
    for record in records:
        r = record.split()
        h,m = r[0].split(":")
        time = int(h)*60 + int(m)
        car = r[1]
        log = r[2]
        
        if car not in dic:
            dic[car] = [[time,log]]
        else:
            dic[car].append([time,log])

    arr = sorted(dic.items(), key = lambda x : x[0])
    
    for i in arr:
        t = 0
        for j in i[1]:
            if j[1] == "IN":
                t -= j[0]
            else:
                t += j[0]
            
        if i[1][-1][-1] == "IN":
            t += 23*60 + 59
        
        fee = fees[1]
        if t >= fees[0]:
            fee += ceil(((t-fees[0])/fees[2])) * fees[3]

        answer.append(fee)

    return answer