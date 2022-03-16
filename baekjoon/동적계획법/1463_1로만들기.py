import sys
input = sys.stdin.readline

# 연산 3가지 가능
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

n = int(input())

dp = [0]*(10**6+1)

for i in range(2,n+1):
    # 1을 빼는 경우
    dp[i] = dp[i-1] + 1     # 경우의수 +1
    
    # 2로 나누어 떨어지는 경우
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)    # 그대로 or 경우의수 +1
        
    # 3으로 나누어 떨어지는 경우
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
        
print(dp[n])

