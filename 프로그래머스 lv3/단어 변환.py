from collections import deque
def solution(begin, target, words):
            
    if target not in words:
        return 0
    
    q = deque([(begin,0)])    
    while q:
        now,cnt = q.popleft()
        if now == target:
            return cnt
        
        for i in words:
            gap = 0
            for a,b in zip(now,i):
                if a!=b:
                    gap += 1

            if gap == 1:
                q.append((i,cnt+1))