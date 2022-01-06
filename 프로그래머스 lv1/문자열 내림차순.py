def solution(s):
    arr = []
    arr.extend(s)
    arr.sort(reverse=True)

    answer = ''
    for i in arr:
        answer += i

    return answer