# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
cnt = [0]*5
lost = [2,4]
reserve = [1,3,5]
n = 5

def solution(n, lost, reserve):
    
    # 여분 가져온 애가 도난당했을 경우때문에
    # 1. 도난 명단에서 제거(여분으로 채울거니까)
    # 2. 여분 명단에서 제거(여분 쓸거니까)
        
    lost2 = list(set(lost)-set(reserve))    # 여기서 lost가 바뀌므로, lost2 따로 생성 
    reserve2 = list(set(reserve)-set(lost)) 
    
    cnt = 0
    for i in lost2:
        if i-1 in reserve2:
            reserve2.remove(i-1)
            cnt += 1
        elif i+1 in reserve2:
            reserve2.remove(i+1)
            cnt += 1
            
    return n-len(lost2)+cnt