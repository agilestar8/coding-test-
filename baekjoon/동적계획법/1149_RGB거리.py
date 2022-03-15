import sys
input = sys.stdin.readline

n = int(input())
dp = [] # 누적 최소값

for i in range(n):
    a,b,c = map(int,input().split())
    dp.append([a,b,c])

# dp[0][0:2]는 초기값

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0] # 현재 빨간색 선택했다면, 이전 다른 두 색깔 중 최소 비용 더해서 갱신
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1] # 현재 초록색 선택했다면, 이전 다른 두 색깔 중 최소 비용
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2] # 현재 파랑색 선택했다면, 이전 다른 두 색깔 중 최소 비용

print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])) # 셋 중 최소비용 출력
 