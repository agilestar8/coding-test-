t = int(input())
for _ in range(t):
    
#  1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16

    n = int(input())

    dp = [1]*(n+1)

    for i in range(3,n+1):
        dp[i] = dp[i-2] + dp[i-3]
        
    print(dp[n-1])
