def solution(n):
    answer = 0
    arr = []
    l = list(str(n))
    l.sort(reverse=True)

    arr = "".join(l)

    return int(arr)