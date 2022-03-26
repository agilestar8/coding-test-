def solution(n):
  
    dp = [0]*(n+1)
    dp[1] = 1   # 2x1타일 까는 경우 : 세로1개
    dp[2] = 2   # 2x2타일 까는 경우 : 세로2개 or 가로2개 까는 경우 = 2개
    # dp[3] = 3
    # 3번째 부터 중복되므로 DP
    for i in range(3,n+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 1000000007
    
    return dp[n]