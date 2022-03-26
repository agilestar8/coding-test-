def solution(N, number):
    s = [set() for _ in range(8)]  # 최소값 8
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))
        # ex) 5 55 555 5555 ... 55555555

    for i in range(1, len(s)):
        for j in range(i):  # ex 13 22 31 되게..
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer