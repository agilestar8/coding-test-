import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int,input().split()))       # 도시 사이의 거리
oil_fee = list(map(int,input().split()))[:-1]   # 마지막도시는 도착했으므로 기름값 의미없음
min_price = 1e9
answer = 0
for i in range(n-1):            # 항상 현재 도시까지의 최소금액만큼 넣어야함
    if oil_fee[i] < min_price:  # 현재도시의 기름가격이 최소가격이면
        min_price = oil_fee[i]

    answer += min_price * distance[i]  # 그 거리만큼 비용지불

print(answer)


