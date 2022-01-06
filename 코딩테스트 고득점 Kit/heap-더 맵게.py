import heapq as hq

def solution(scoville, K):
    cnt = 0
    hq.heapify(scoville)  # 배열을 heap형태로 만들기

    while 1:
        min1 = hq.heappop(scoville)  # 제일 작은 값 추출
        if min1 >= K:  # 스코빌 지수 만족할 시 종료
            break
        elif len(scoville) == 0:  # 스코빌 지수 만족 불가능 시 -1
            cnt = -1
            break

        min2 = hq.heappop(scoville)  # min1이 나간 후 pop이면 두 번째로 작은 값, 추출
        new_scoville = min1 + min2 * 2
        hq.heappush(scoville, new_scoville)  # scoviile에 새 스코빌지수 삽입
        cnt += 1  # 최소 횟수 +1

    return cnt