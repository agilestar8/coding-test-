def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True) 
    # 각 숫자를 4번씩 반복해(조건에선 수가 1000이하-4자리수) 나온 수를 기준으로 큰 것부터 정렬
    # ex) 5 9 3 30 34 --> 9999 5555 34343434 3333 3030303030 -> 9 5 34 3 30 순서

    if numbers[0] == "0":
        return "0"
    else:
        return "".join(numbers)
    