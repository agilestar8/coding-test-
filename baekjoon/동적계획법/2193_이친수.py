# 0과 1로만 이루어짐
# 이친수는 0으로 시작하지 않는다.
# 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.

# 1자리
# 1 - 1개

# 2자리
# 10 - 1개

# 3자리
# 100 101 - 2개

# 4자리
# 1000 1010 1001 - 3개

# 5자리
# 10000 10100 10101 10001 10010 - 5개

# 6자리
# 100000 101000 100100 100010 100001 101010 101001 100101 - 8개

n = int(input())
dp = [0]*(91)
dp[1] = 1
dp[2] = 1
for i in range(3,91):
    dp[i] = dp[i-1] + dp[i-2]
    
# print(dp)
print(dp[n])


