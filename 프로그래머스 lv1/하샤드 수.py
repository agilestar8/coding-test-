def solution(x):
    a = [int(c) for c in str(x)]

    return True if x % sum(a) == 0 else False