def solution(n):
    answer = 0
    arr = []
    while n >= 1:
        rest = n % 3
        n = n // 3
        arr.append(rest)

    arr = arr[::-1]
    for i in range(len(arr)):
        answer += arr[i]*(3**i)

    return answer