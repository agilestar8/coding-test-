def solution(n):
    answer = ''
    arr = ["수", "박"]
    for i in range(n):
        i = i % 2
        answer += arr[i]

    return answer