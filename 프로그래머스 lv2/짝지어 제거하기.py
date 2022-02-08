from collections import deque

def solution(s):
    s = deque(s)
    q = []  
    
    while s:
        v = s.popleft()     # s에서 원소하나 빼내서
        if q:               # 큐가 존재할 때
            if q[-1] == v:  # 큐의 최근들어온 원소와 같으면
                q.pop()     # 연속으로 같은문자이므로 큐에서 제거하고 추가도 안함
            else:           # 큐의 최근들어온 원소와 다르면
                q.append(v) # 큐에 추가
        
        else:               # 큐가 원소가 없으면
            q.append(v)     # 큐에 추가

    if not q:       # 큐가 비었다면
        return 1    # 전부 지운것이므로 1
    else:           # 큐가 남았다면
        return 0    # 전부 못지웠으므로 0