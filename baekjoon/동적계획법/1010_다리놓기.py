t = int(input())
for _ in range(t):

    n,m = map(int,input().split())
    # case1) DP로 풀기
    dp = [[0]*(m+1) for _ in range(n+1)]
    # 0 1 2 3 4 m
    # 1 1 2 3 4 5  6  7
    # 2 0 1 3 6 10 15 21 ...
    # 3 0   1
    # n       1
    for i in range(n+1):
        for j in range(m+1):
            if i == 1:
                dp[1][j] = j # 서쪽이 1개면, 동쪽루트는 동쪽 다리개수만큼
                
            elif i == j: # 같은 다리 수면, 모든 경우 1
                dp[i][j] = 1
                
            elif i<j: # 그 외 점화식
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                
    print(dp[n][m])


# case2) 조합으로 풀기
# answer = factorial(m) // (factorial(n) * factorial(m-n))
# print(answer)