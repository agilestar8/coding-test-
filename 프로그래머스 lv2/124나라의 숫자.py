def solution(n):
    answer = ''
    numlist = '124' # 1,2,4만 사용하여 숫자를 표현해야함

    while n > 0:
        n -= 1  # 1을 넣으면 numlist의 0번째 index부터 제대로 시작
        answer = numlist[n%3] + answer
        n //= 3

    return answer