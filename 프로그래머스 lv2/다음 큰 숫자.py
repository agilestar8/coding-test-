def binary_number_of_one(n):
    arr = []
    while n > 0:
        rest = n % 2
        n //= 2
        arr.append(rest)

    num_of_one = sum(arr)
    return num_of_one

def solution(n):
    m = n + 1
    while True:
        if binary_number_of_one(m) == binary_number_of_one(n):
            break
        else:
            m += 1

    return m
