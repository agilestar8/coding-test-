import heapq
def solution(operations):
    
    q = []
    for i in operations:
        d,num = i.split()
        
        if d == "I":
            heapq.heappush(q,int(num))
        
        else:
            if q: # 빈 큐에서 삭제는 무시
                if '-' in num:  # 최소값 삭제
                    heapq.heappop(q)
                else:
                    q.pop()
         
    if q:
        return [max(q),min(q)]
    else:
        return [0,0]