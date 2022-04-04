def solution(n):
    answer = []
    hanoi(n,1,3,2,answer) 
        
    return answer

def hanoi(n,start,end,mid,answer): 
    if n == 1:
        answer.append([start,end]) # start에서 end로 옮김
    
    else:
        hanoi(n-1,start,mid,end,answer) # n-1개를 start에서 mid로 옮김
        answer.append([start,end])      # 남은 한개를 end로 
        hanoi(n-1,mid,end,start,answer) # 나머지 n-1개를 mid에서 end로