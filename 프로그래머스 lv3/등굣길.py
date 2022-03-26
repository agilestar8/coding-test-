def solution(m, n, puddles):
    
    dp = [[0]*(m+1) for _ in range(n+1)]
        
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == j == 1: # 초기화, (1,1)은 경우의 수1
                dp[1][1] = 1
            
            elif [j,i] not in puddles:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
    # print(dp[n][m])
    
    return dp[n][m]%1000000007