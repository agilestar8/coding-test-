import math

def solution(n):
    x = math.sqrt(n)
    if x/int(x) == 1.0:
        return((x + 1) ** 2)
    else:
        return -1