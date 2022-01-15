import sys
input = sys.stdin.readline
# f(x)는 다음과 값 중 최솟값을 가진다.
# 1) f(x-1) + 1
# 2) f(x/2) + 1
# 3) f(x/3) + 1

n = int(input())
dp = [[0, []] for _ in range(n + 1)]    # n+1개의 DP리스트 (횟수,계산중인 숫자)
                                        # 10에서 줄어들기만 할것이므로 n+1개 리스트

dp[1][0] = 0    # 1부터시작, 연산횟수는 0
dp[1][1] = [1]  # 계산과정을 담는 리스트, 1을 먼저 담음
# -> [0,[1]]    # 횟수0, 현제 과정[1]

for i in range(2, n + 1):   # 초기값 1제외, 2부터 시작

    # 1) f(x-1) + 1
    dp[i][0] = dp[i-1][0] + 1       # 이전보다 횟수 +1
    dp[i][1] = dp[i-1][1] + [i]     # 
    
    # 2) f(x/2) + 1
    if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]
        
    # 3) f(x/3) + 1
    if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]
    
print(dp)
print(dp[n][0])
print(*reversed(dp[n][1]))


