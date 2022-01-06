def solution(n, lost, reserve):
    s = set(lost) & set(reserve)  # 잃어버렸지만 여분있어서, 못빌려주지만 참가가능
    l = set(lost) - s  # 진짜 없는 학생
    r = set(reserve) - s  # 빌려줄 수 있는 학생

    for x in sorted(r):  # 빌려줄 수 있는 학생 중에서
        if x - 1 in l:  # 자신의 앞번호가 없는 학생이면
            l.remove(x - 1)  # 빌려주고 없는 사람 명단에서 제거
        elif x + 1 in l:
            l.remove(x + 1)

    return n - len(l)