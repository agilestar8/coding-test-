from collections import deque

def solution(number, k):
    number = deque(list(map(int,number)))
    q = []
    l = len(number)
    
    while number:
        n = number.popleft()
        while q and k > 0 and q[-1] < n:  # 지울횟수 남았다면
            q.pop()
            k -= 1
        q.append(n)
    
    answer = ""    
    for i in q:
        answer += str(i)
    return answer[:l-k]


