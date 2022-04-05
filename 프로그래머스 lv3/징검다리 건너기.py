# 연속된 0돌 개수가 k이하여야한다
# answer
def solution(stones, k):
    answer = 0
    # 연속된 0돌 개수가 k이하여야한다 
    
    left = 1 # 최소
    right =  200000000# 최대 
    
    while left <= right: 
        mid = (left+right)//2

        # 연속되는 0돌 체크
        seq = 0
        for i in stones:
            if i <= mid:
                seq += 1
            else:
                seq = 0
            
            if seq >= k: # k를 넘는순간 중지해야 시간초과안걸림, 다 구하고 max()는 시간초과
                break
                    
        if seq < k:       # 감당가능하면 
            left = mid+1  # 사람 수 늘려보고
        else:             # 감당불가능하면
            right = mid-1 # 사람 수 줄여보기
                          
    return left


# case2 
def solution2(stones, k):
    answer = 0
    n = len(stones)
        
    
    while True:  
        answer += 1
        for i in range(n):
            if stones[i] > 0:
                stones[i] -= 1

        zcnt = 0
        for j in stones:
            if j == 0:
                zcnt += 1
                if zcnt == k:
                    return answer
            else:
                zcnt = 0