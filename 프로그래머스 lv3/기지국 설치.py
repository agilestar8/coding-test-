from math import ceil
def solution(n, stations, w):
    answer = 0

    # 두 기지국 사이의 빈칸(거리)를 구해야함
    distance = []
    for i in range(len(stations)-1):
        right = stations[i]+w
        left = stations[i+1]-w
        distance.append(left-right-1)

    # 맨 처음칸과 첫 기지국, 맨 뒷칸과 마지막 기지국 사이의 빈칸 수 계산
    a = (stations[0]-w) - 1
    b = n - (stations[-1]+w)
    distance.append(a)
    if b > 0: distance.append(b) 
    print(distance)
    
    # 빈칸들을 2w+1로 몇개씩 커버 가능한지 확인 후, 올림
    for i in distance:
        answer += ceil(i / (2*w+1))
               
    return answer