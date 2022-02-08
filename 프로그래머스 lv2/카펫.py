def solution(brown, yellow):

    area = brown + yellow
    
    for a in range(1,area//2):  # 1부터 시작
        if area % a == 0:       # 넓이가 a로 나눠지고
            if area//a <= a:    # a(가로)가 b(세로)보다 길고
                b = area//a     
                if 2*a + 2*b == brown + 4:  # 규칙을 만족하면
                    return [a,b]

    # 1. (a-2)(b-2) = area
    # 2. 2a + 2b - 4 = brown