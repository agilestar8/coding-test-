def solution(numbers):
    answer = []
    # 비트패턴에서
    # 00 --> 01로 
    # 01 --> 10로 
    # 10 --> 11로 변화
    
    for div in numbers:
        if div < 2:
            answer.append(div+1)
            continue

        binary = []    
        while div:
            div, mod = divmod(div, 2)
            binary.append(mod) 
            # binary는 뒤집혀있는 이진수
            
        # 왼쪽부터 서치해서 (이진법 오른쪽부터)
        for i in range(len(binary)-1):
            # 0'0' -> 0'1' 
            # 1'0' -> 1'1'
            if binary[i:i+2] == [0, 0] or binary[i:i+2] == [0, 1]:
                binary[i] = 1
                break
                
            # 01 -> 10
            if binary[i:i+2] == [1, 0]:
                binary[i:i+2] = [0, 1]
                break
        
        # for문에 안걸렸다면
        else:
            binary[-1] = 0 # 가장작은 1비트 추가
            binary.append(1)

        base10 = 0
        for i in range(len(binary)):
            base10 += binary[i] * 2 ** i
        answer.append(base10)
        
    return answer