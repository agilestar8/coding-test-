n = int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))

answer = 0

min_price = 1e9

# 비용 = 다음 도시까지 거리 x 최소 기름값(갱신해야함)
for i in range(n-1):
    if price[i] < min_price:
        min_price = price[i]

    cost = min_price * dist[i]
    answer += cost

print(answer)

