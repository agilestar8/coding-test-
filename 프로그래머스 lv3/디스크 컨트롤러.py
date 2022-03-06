import heapq
def solution(jobs):
    # idea : 매 시각마다 요청받은 작업중에서, 소요시간이 적게 걸리는 것부터 하기
    answer = 0
    n = len(jobs)
    now = 0
    start = -1
    done = 0
    q = []
    
    while done < n: # 작업 다 할때까지
        for i,j in jobs: 
            if start < i <= now: # 요청이 왔었다면
                heapq.heappush(q, [j,i])    # disk에 작업올려놓기(짧은작업 우선순서로)
            
        if q: # 작업이 있다면
            a,b = heapq.heappop(q)  # 작업하기
            start = now             # start~현재시간사이 작업은 한번에 다 받았으므로 그 종료시간 이후 요청부터 받기
            now += a                # 현재시간 갱신, 작업시간만큼 시간+
            answer += now-b         # (종료시간-요청시간) 구하기
            done += 1               # 작업수 +1
        else:
            now += 1                # 작업없으면 시간+1
            
    return answer//n