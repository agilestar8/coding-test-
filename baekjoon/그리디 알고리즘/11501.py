import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    n = int(input())
    price = list(map(int,input().split()))
    max_price = 0
    profit = 0
        
    for i in range(n-1,-1,-1):      # 최대주식가격을 미래-->과거로 서치
        if max_price < price[i]:    # 미래보다 과거가 가격이 더 높아지면
            max_price = price[i]    # 최대가격 갱신

        else:
            profit += max_price - price[i]    # 최고가격-현재가격만큼 이득
        
    print(profit)

# 1 1 3 1 2 -> 2에서1에서 1이득, 1에서 2->3으로갱신, 3에서1에서 2이득, 3에서1에서 2이득