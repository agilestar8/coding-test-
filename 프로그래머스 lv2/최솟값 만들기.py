def solution(a, b):
    s = 0
    a.sort()
    b.sort(reverse=True)

    while a and b:
        f1 = a.pop()
        f2 = b.pop()
        s += f1 * f2

    return s