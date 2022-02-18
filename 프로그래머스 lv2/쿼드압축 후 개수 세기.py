def solution(arr):
    answer = [0,0] # [0개수,1개수]
    n = len(arr)
    
    def compress(n,a,b):
        temp = arr[a][b]
        for i in range(a,a+n): # 정사각형 모든 값에 대해서
            for j in range(b,b+n): 
                if arr[i][j] != temp: # 압축 불가능이면
                    # 4분할 재귀
                    n = n//2
                    compress(n,a,b)
                    compress(n,a+n,b)
                    compress(n,a,b+n)
                    compress(n,a+n,b+n)
                    return # 압축 불가능한, 4분할 하기전의 재귀는 종료

        # 압축가능하면
        answer[temp] += 1
    
    compress(n,0,0)    
    return answer
    