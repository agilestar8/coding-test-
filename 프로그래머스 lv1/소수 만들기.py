def isPrime(n):
    num = set(range(2, n + 1))  # 2부터 주어진 수 까지의 set배열
    for i in range(2, int(n ** 0.5) + 1):  # i는 2부터 주어진 수까지 돌면서
        if i in num:  # i가 num배열에 있으면
            num -= set(range(2 * i, n + 1, i))  # 남은 배열은 소수만 남게된다

    if n in num:
        return True
    else:
        return False

def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if isPrime(nums[i] + nums[j] + nums[k]):
                    answer += 1

    return answer