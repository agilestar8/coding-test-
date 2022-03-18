n = int(input())
arr = list(map(int,input().split()))

dp = [0]*n
dp[0] = arr[0] # 초기화, 맨처음 dp[0]은 배열 첫 숫자

# 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 
# 왼쪽 부터 차근차근 더하면서 큰 숫자가 나올 경우 DP 배열에 넣어준다.
# --> 이전 dp합에서 현재 배열숫자를 더해서 더 커지면 업데이트, 작아지면 더 큰 숫자로 교체

for i in range(1,n):
    dp[i] = max(arr[i], dp[i-1]+arr[i]) 

# print(dp)
print(max(dp))