n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))

# 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

dp = [0]*(n+1)
dp[1] = wine[1]
if n > 1:
    dp[2] = wine[1]+wine[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i], dp[i-1]) 
    # 연속으로 1,2,3번잔을 마실 수 없을때, 3개의 잔까지 최대값은 
    # 1) 1번잔 + 3번잔 
    # 2) 2번잔 + 3번잔 
    # 3) 1번잔 + 2번잔 (3번잔 그냥 안먹기)
    
print(max(dp))
