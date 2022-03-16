import sys
input = sys.stdin.readline

#         7
#       3   8
#     8   1   0
#   2   7   4   4
# 4   5   2   6   5
# 삼각형에서 내려갔을 때, 가장 큰 누적합 구하기

n = int(input())

dp = []
for _ in range(n):
    dp.append(list(map(int,input().split())))
    
for i in range(1,n):
    for j in range(len(dp[i])):
        if j == 0: # 맨 왼쪽은 위에서밖에 못받음
            dp[i][j] = dp[i][j] + dp[i-1][j] # 3+7
        elif j == len(dp[i])-1: # 맨 오른쪽은 오른쪽위 에서밖에 못받음
            dp[i][j] = dp[i][j] + dp[i-1][j-1] # 8+7
        else: # 그 외에는 양쪽에서 받은 거 더한 후 큰 값으로
            dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j])
                
print(max(dp[n-1]))

