def solution(priorities, location):
    queue = [(p,i) for i,p in enumerate(priorities)]
    answer = 0

    while len(queue):
        now = queue.pop(0)
        if queue and now[0] < max(queue)[0]:
            queue.append(now)
        else:
            answer += 1
            if now[1] == location:
                break

    return answer
