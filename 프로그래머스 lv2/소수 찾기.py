from itertools import permutations

def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def solution(numbers):
    cnt = 0
    arr = []
    for i in range(1, len(numbers) + 1):
        arr += (list(permutations(numbers, i)))
    arr2 = set([int("".join(i)) for i in arr])

    for i in arr2:
        if isPrime(i) == True:
            cnt += 1

    return cnt