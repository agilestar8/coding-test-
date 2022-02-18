def solution(n, left, right):
    arr = []
    for i in range(left,right+1):
        # 규칙성 : i번째 좌표에 대해 (i//n, i%n)중 큰 것을 row, 작은것을 column로 표현하면됨
        # 시간 줄이기위해, left ~ right까지
            a = i//n
            b = i%n
            a = max(a,b)
            arr.append(a+1)

    return arr    
