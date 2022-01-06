import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 우선순위 큐 사용
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식 개수

    # sum_value + (현재 제일 작은 음식시간-이전음식시간) * 현재 음식개수 와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]  # 현재 제일 적게 걸리는 음식의 시간
        sum_value += (now - previous) * length  # 그 음식을 다 먹는데 걸리는 시간
        length -= 1  # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    # 남은 음식 정렬하고
    result = sorted(q, key=lambda x: x[1])
    # 남은 시간 % 남은 음식개수의 인덱스를 가진 음식번호를 반환
    return result[(k - sum_value) % length][1]