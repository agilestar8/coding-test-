# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
cnt = [0]*5
lost = [2,4]
reserve = [1,3,5]
n = 5

def solution(n, lost, reserve):
    answer = 0 
    for i in range(1, n+1): # 1번부터 5번까지
        if i not in lost: #안 잃어버린 학생은
            answer += 1 # 수업 참가 가능
            
        else: # 잃어버린 학생중에
            if i in reserve: #여분 있는 학생이면
                answer += 1 # 수업 참가 가능
                reserve.remove(i) # 여분에서 꺼내입음
                lost.remove(i) # 잃어버린 것 땜빵으로 해결했으니 명단에서 제외

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve: # 앞 번호학생이 여분이 있으면
            answer += 1 # 빌려받고 수업 참가 가능
            reserve.remove(i-1) # 빌림

        elif i+1 in reserve: # 앞번호는 여분 없고, 뒷 번호학생이 여분 있으면
            answer +=1 # 빌려서 참가 가능
            reserve.remove(i+1)

    return answer
