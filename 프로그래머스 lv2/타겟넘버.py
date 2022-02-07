from collections import deque

def solution(numbers, target):
    
    q = deque([(0,0)])  # 초기값0, 인덱스0
    case = 0
        
    while q:
        now,idx = q.popleft()

        if idx == len(numbers):
            if now == target:
                case += 1
        else:
            for i in [numbers[idx], -numbers[idx]]: # 더하거나 빼거나, 둘중하나
                q.append((now+i,idx+1))             # 다음큐에 인덱스+1로 추가
 
    return case

print(solution([1, 1, 1, 1, 1],3))