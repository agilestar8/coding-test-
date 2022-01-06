n = int(input())
coin = list(map(int,input().split()))
coin.sort()

target = 1  # 1을 만들 수 있냐 부터 시작

for i in coin:  # 제일 작은 동전부터 시작
    if i > target:  # 못 만드는 경우
        break   
    target += i

print(target)

# 5
# 3 2 1 1 9