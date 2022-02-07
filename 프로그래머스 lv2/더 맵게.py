import heapq

def solution(scoville, K):
    
    cnt = 0
    heapq.heapify(scoville)

    while len(scoville)>=2:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = a+2*b
        heapq.heappush(scoville, c)
        cnt += 1    # 1회 섞었음
        
        if scoville[0] >= K:    # 제일 안매운게 K 이상이면
            break               # 종료

    if scoville[0] >= K:       # 하나남아도, K보다 매우면
        return cnt
    else:                       # 하나남았는데 K보다 덜 매우면
        return -1

# [1, 2, 3, 9, 10, 12]	7	2
print(solution([1, 2, 3, 9, 10, 12],7))
