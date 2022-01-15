import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

dp = [n+1] * n 
dp[0] = 0

# arr의 다음idx = 현재idx + 배열의값arr[i] 이므로

for i in range(n):  # 현재 인덱스들에서
    for j in range(1, arr[i]+1):    # 1 ~ 배열의값 중 
        if i+j >= n:    # i+j(인덱스+배열의값)이 10번째를 넘으면
            break       # 도착했으므로 중지

        dp[i+j] = min(dp[i+j], dp[i]+1)     # (idx+배열값)과 (현재값+1)중 적은 것 저장
        
print(dp[n-1] if dp[n-1] != n+1 else -1)
    
# if dp[n-1] != n+1:
#     print(dp[n-1])
# else:
#     print(-1)
    
    