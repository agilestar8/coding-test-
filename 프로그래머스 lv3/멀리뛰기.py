def solution(n):

    if n < 3:
        return n
    
    # DP
    dp = [0]*(n+1)
    dp[1] = 1       # 1칸가는 방법 1가지 ([1])
    dp[2] = 2       # 2칸가는 방법 2가지 ([1,1],[2])
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]%1234567