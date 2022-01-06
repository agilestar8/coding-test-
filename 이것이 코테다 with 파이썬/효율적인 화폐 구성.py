n, m = 2, 15 # 화폐단위 n개로 m원을 만들어라

coin = []
for i in range(n):
    coin.append(int(input()))

# dp 테이블 초기화
d = [10001] * (m+1)
d[0] = 0                # 0원을 만드는 경우는 0개의 화폐를 쓰는 것

# dp 진행 : 바텀업
for i in range(n): # n번 
    for j in range(coin[i], m+1):   # 각 화폐 단위 마다
        if d[j-coin[i]] != 10001:   # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-coin[i]]+1)

# 계산 결과
if d[m] == 10001:   # 불가능 - m원을 만들 방법이 없는 경우
    print(-1)
else:
    print(d[m])

