n,k = map(int,input().split())

dp = [[1] * (i+1) for i in range(1001)]

for i in range(2,1001):     # 2번째 줄 ~ 1000번째 줄까지
    for j in range(1,i):    # 줄 수 = 원소 수
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][k] % 10007)

