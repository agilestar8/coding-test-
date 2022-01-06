def balance_idx(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            return i


def is_proper(p):
    cnt = 0
    for i in p:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return False
    if cnt == 0:
        return True
    else:
        return False


def solution(p):
    answer = ""

    # 1.
    if p == "":
        return answer

    # 2.
    idx = balance_idx(p)
    u = p[:idx + 1]
    v = p[idx + 1:]

    # 3.
    if is_proper(u):
        answer = u + solution(v)
    # 4.
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("

        answer += "".join(u)

    return answer
