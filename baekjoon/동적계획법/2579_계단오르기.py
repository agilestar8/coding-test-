import sys
input = sys.stdin.readline

n = int(input())
stair = [0]
for _ in range(n):
    stair.append(int(input()))

if n == 1:
    print(stair[1])

else:
    dp = [0]*(301)      # dp는 n번째 계단에서의 누적 최대값
    dp[1] = stair[1]          # 1칸의 최대값 = 그냥 1칸의 값
    dp[2] = stair[1]+stair[2] # 2칸의 최대값 = 1칸+2칸의 합

    for i in range(3,n):    # 3번째칸부터, 3번전 누적+1번전+현재칸(2칸뛰고+1칸뛰기) vs 두번전 누적+현재칸(2칸뜀) 중 큰 값
        dp[i] = max(dp[i-3]+stair[i-1], dp[i-2]) + stair[i]
        
    print(dp[n])
