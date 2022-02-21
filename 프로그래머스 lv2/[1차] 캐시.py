from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque([])
    
    for i in cities:
        i = i.upper()
        if i in q: # cache hit
            answer += 1 
            q.remove(i) # 캐시에 있었어도, 맨 뒤를 바꿔줘야함
            q.append(i)
            
        else:  # cache miss
            if len(q) < cacheSize:
                q.append(i)
            else:
                q.append(i)
                q.popleft()
            answer += 5

    return answer