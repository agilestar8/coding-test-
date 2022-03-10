import heapq
def solution(n, works):
    answer = 0
    # 야근지수 최소로 하기
    # -> 제곱으로 늘어나기때문에 일의 양을 골고루만들어야함
    # 힙큐로 최대값 추출해서 빼기
    
    q = []
    for i in works:
        heapq.heappush(q, (-i,i)) # 최대값순으로 뺄 수 있게
    
    while n!=0:
        a,b = heapq.heappop(q)    # 최대값 빼내서
        b -= 1                    # 1감소 시키고
        if b < 0:
            break
        heapq.heappush(q, (-b,b)) # 다시 넣기
        n -= 1
        
    for i,j in q:
        answer += j**2
    return answer