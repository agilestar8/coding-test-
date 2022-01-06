def solution(n):
    answer = 0

    for k in range(1, n + 1):
        start = k
        s = 0

        for i in range(start, n + 1):
            s += i
            if s > n:
                break
            elif s == n:
                answer += 1

    return answer