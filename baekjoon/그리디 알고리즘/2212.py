import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = list(map(int,input().split()))

# n개의 센서를 최소거리의 k개로 분류하기

if k >= n:      # 기지국이 더 많으면
    print(0)    # 모든 센서가 제자리에서 수신가능 = 거리합 0

else:
    arr.sort()  # 센서 오름차순 정렬

    sensor_dist = []    # 센서 간 거리
    for i in range(n-1):
        sensor_dist.append(arr[i+1]-arr[i])

    sensor_dist.sort()  # 센서 간 거리 정렬

    for i in range(k-1):    # k개의 기지국으로 분리하므로, k-1번
        sensor_dist.pop()   # 센서 간 거리들 중, 가장 큰 거리순서로 제거
        
    print(sum(sensor_dist)) # 남은 k-1개 구역의 거리의 합은 최소센서거리의 합


