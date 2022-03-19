n = int(input())
arr = [0] + list(map(int,input().split()))

# 최대한 돈 많이써서 n개의 카드를 구매해라
dp = [0]*(n+1) # dp[n] : n개의 카드를 구매하는 최대가격
dp[1] = arr[1]

# d[2] = d[1] + p[1] or d[0] + p[2]
# d[3] = d[2] + p[1] or d[1] + p[2] or d[0] + p[3]
# d[4] = d[3] + p[1] or d[2] + p[2] or d[1] + p[3] or d[0] + p[4]

for i in range(2,n+1):
    for j in range(1, i+1): # i가 3장이면, j는 1~3장 까지 => (dp[1],arr[2]) (dp[2],arr[1]) (dp[0],arr[3]) 
        if dp[i] < dp[i-j]+arr[j]:  # dp[i] = i까지 산 최대금액에서, j장 만큼 빼서 따로 사는 경우 점화식 : dp[i-j]+arr[j]
            dp[i] = dp[i-j]+arr[j]  # 따로 산게 더 크면 교체

print(dp[n])