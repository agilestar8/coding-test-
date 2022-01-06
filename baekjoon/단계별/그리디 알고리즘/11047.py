n,k = map(int,input().split())
coin = []

for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

answer = 0

for i in coin:
    if k == 0:
        break
    if i <= k:
        answer += k // i
        k %= i
print(answer)







