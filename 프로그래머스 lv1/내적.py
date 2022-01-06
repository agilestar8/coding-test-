def solution(a, b):
    answer = 0

    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                answer += (a[i] * b[j])

    return answer