# 구조가 가능한지 판별
def possible(answer):
    for x,y,stuff in answer:
        if stuff == 0:  # 기둥이면
            # 바닥 or 보의 한쪽(왼/오) 끝부분 or 다른 기둥 위면 정상
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False

        elif stuff == 1: # 보면
            # 한쪽 끝부분이 기둥 위 or 양쪽 끝부분이 다른 보와 동시에 연결이면 정상
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x,y,stuff,operate = frame

        if operate == 1:    # 설치 작업
            answer.append([x,y,stuff])  # 일단 설치하고
            if not possible(answer):    # 가능한지 체크
                answer.remove([x,y,stuff])

        if operate == 0:    # 삭제 작업
            answer.remove([x,y,stuff]) # 일단 삭제하고
            if not possible(answer):    # 구조물이 가능한지 체크
                answer.append([x,y,stuff])  # 불가능 시 다시 설치
        
    return sorted(answer)
            
n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# answer = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(n,build_frame))


