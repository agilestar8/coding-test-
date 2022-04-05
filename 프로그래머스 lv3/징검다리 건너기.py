# 연속된 0돌 개수가 k이하여야한다
# answer



# case2 
def solution(stones, k):
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