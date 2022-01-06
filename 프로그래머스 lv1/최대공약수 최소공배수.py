def solution(a, b):
    answer = []
    n, m = a, b
    # 최소공배수 = n * m / 최대공약수
    # 최소공약수 - 유클리드 호제법
    if a < b:
        a, b = b, a
    while b != 0:
        (a, b) = (b, a % b)

    gcd = a
    lcm = n * m // gcd
    answer.append(gcd)
    answer.append(lcm)

    return answer