def solution(s):
    cnt = 0
    zero = 0
    while s != '1':
        for i in s:
            if i == "0":
                zero += 1
        s = s.replace("0", "")
        c = len(s)
        s = format(c, 'b')
        cnt += 1

    return [cnt,zero]
