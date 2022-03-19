t = int(input())
for _ in range(t):

    n = int(input())
    dp = [list(map(int,input().split())) for _ in range(2)]
    # 1번줄과 2번줄의 포인트는
    # 1번전의 대각 누적포인트합, 2번전의 대각 누적포인트합중 큰 것을 더해나가기

    for i in range(1,n):
        if i == 1: # 초기값 설정
            dp[0][1] += dp[1][i-1]
            dp[1][1] += dp[0][i-1]
            
        else: # 점화식
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])  
            dp[1][i] += max(dp[0][i-1], dp[0][i-2]) 

    print(max(dp[0][n-1],dp[1][n-1]))
