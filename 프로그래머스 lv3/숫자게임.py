def solution(A, B):
    answer = 0
    
    n = len(A)
    # n번의 대결 중 최대한 많이 이기기
    # A - 1 3 5 7
    # B - 2 2 6 8
    
    # 투 포인터 알고리즘
    A.sort()
    B.sort()
    j = 0

    for i in range(n):  # B가 증가하면서
        if A[j] < B[i]: # 조건에 맞으면, A,B 둘다 증가
            answer += 1
            j += 1 # A증가
        
        # 안맞으면 다음 B 서치
    return answer