import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):

    n = int(input())
    dp = [0]*(11)
    dp[1] = 1 # 1
    dp[2] = 2 # 11 2
    dp[3] = 4 # 111 21 12 3
    dp[4] = 7 # (111 21 12 3)에 1 추가한 경우 + (11 2)에서 2 추가한 경우 + (1)에 3추가한 경우의 합
              # 1111 211 121 31 + 112 22 + 13
              # 4+2+1 = 7 => 이전거 3개의 합

    for i in range(4,11):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    print(dp)
