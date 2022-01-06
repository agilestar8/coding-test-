## 동적계획법
def solution(n):
    memo = [0 for i in range(n + 1)]
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = (memo[i - 1] + memo[i - 2]) % 1234567

    return memo[n]

## 간단풀이
def solution2(n):
    f1,f2 = 0,1

    for i in range(n):
        f1, f2 = f2, f1 + f2

    return f1 % 1234567
