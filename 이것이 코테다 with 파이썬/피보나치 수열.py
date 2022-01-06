def fibonacci(n):

    if n == 1 or n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(20))


## memoization + 재귀
d = [0] * 100
def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:  # 메모 되있으면
        return d[x] # 그거 그대로 씀

    d[x] = fibo(x-1) + fibo(x-2)  # 메모 안되있으면 점화식대로 메모 적음
    return d[x] # 메모 리턴

print(fibo(99))