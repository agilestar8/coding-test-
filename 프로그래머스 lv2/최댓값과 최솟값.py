def solution(s):
    ans = ''

    a = list(map(int, s.split(" ")))
    ans = str(min(a)) + " " + str(max(a))

    return ans