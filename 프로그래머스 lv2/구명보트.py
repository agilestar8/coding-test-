from collections import deque

def solution(people, limit):    
    # 보트는 2명 제한
    # 즉, 맨 앞뒤에서 한명씩 태울 수 있으면 최대효율
    # 근데 무게 초과시, 그냥 맨뒤에서 하나만 태우기
    people.sort()
    q = deque(people)
    boat = 0

    while len(q) > 1:          
        if q[0]+q[-1] <= limit:
            q.popleft()
            q.pop()
            boat += 1
        else:
            q.pop()
            boat += 1
            
    if len(q) == 1:
        return boat+1
    else:
        return boat