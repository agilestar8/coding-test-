def solution(n):
    answer = []

    while (n > 0):
        a = n % 10
        n = n // 10
        answer.append(a)

    return answer