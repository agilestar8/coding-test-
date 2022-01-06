def solution(numbers):
    arr = list(map(str,numbers))                    #1. 사전 값으로 정렬하기
    arr.sort(key=lambda x: x*3, reverse=True)       #2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교

    return str(int(''.join(arr)))
