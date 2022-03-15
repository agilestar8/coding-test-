import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

dp = [1]*(n) # dp[n] : n번째 수를 마지막 원소로 가지는 lis의 길이 

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1) # j가 i번째보다 작을 때, 
                                        # j번째를 마지막으로 하는 것의 LIS에 i를 추가하면, i를 마지막으로하는 LIS이고 개수+1됨

print(max(dp))
