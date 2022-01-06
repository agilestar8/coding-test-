# sol.1
# def solution(n):
#     answer = 0
#     n = str(n)
#     for i in n:
#         answer += int(i)
#
#     return answer

# sol2
def solution(n):
    answer = 0

    while n >= 10:
        a = n // 10  # 몫
        b = n % 10  # 나머지
        n = a
        answer += b
    answer += n

    return answer