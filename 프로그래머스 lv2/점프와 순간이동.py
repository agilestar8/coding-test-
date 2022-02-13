# 뒤에서부터 반 씩 줄여가며, 점프횟수를 찾기

def solution(n):
    jmp = 1
    while n>1:
        if n%2 == 0: # 짝수면, 그냥 반 접고
            n=n//2       
            
        else:       # 홀수면, 1빼고(점프)하고 반 접음
            n=(n-1)//2
            jmp += 1    # 점프횟수 +1

    return jmp

# 최적화
# def solution(n):
#     answer = 1
#     while n > 1:
#         answer += n % 2
#         n = n // 2
#     return answer
    

    
    



