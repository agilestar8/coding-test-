n = int(input())

dp = [0]*31
dp[0] = 1
dp[2] = 3 # 2배수는 3가지 경우가 있음
# 근데 그렇다고 4를 2/2로 봐서 3x3=9가지 경우라고 하면 틀림
# 특수한 2가지 경우를 +해줘야함 -> dp[4] = 3x3 +2 = 11
# dp[6] = 3x3x3 + dp[2]*4 + 2


for i in range(4,31,2):
    dp[i] = dp[i-2]*3
    for j in range(0,i-2,2):
        dp[i] += dp[j]*2

print(dp[n])
