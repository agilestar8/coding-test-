def solution(arr):
    answer=[0,0]
    n=len(arr)
    
    def compression(a,b,l):
        start=arr[a][b]
        for i in range(a,a+l):
            for j in range(b,b+l):
                if arr[i][j]!=start: # 정사각형의 모든 원소가 다르면, 압축 불가능

                    # 4분할하면서 재귀해야함                    
                    l=l//2
                    compression(a,b,l)
                    compression(a,b+l,l)
                    compression(a+l,b,l)
                    compression(a+l,b+l,l)
                    return
                
        answer[start]+=1    # 압축된 값의 개수 +1
        
    compression(0,0,n)
    
    return (answer)