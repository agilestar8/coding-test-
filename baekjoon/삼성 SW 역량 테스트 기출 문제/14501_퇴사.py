n = int(input())
tp = []
for _ in range(n):
    tp.append(list(map(int,input().split())))

dp = [0]*(n+1)

for i in range(n-1,-1,-1):
    if i + tp[i][0] <= n:
        dp[i] = max(tp[i][1]+dp[i+tp[i][0]], dp[i+1])
        
    else:
        dp[i] = dp[i+1]
        
print(dp[0])