import sys
input = sys.stdin.readline

# 주어진 배열의 숫자들의 합으로, 조합할 수 없는 최소 숫자 찾기
# 1 1 2 6 이란 4개의 추가 존재할 때
# 무게 4까지는 조합이 가능하지만, 무게 5는 4(여태까지 추의 합) + 1  >= 6 이 성립이 안되기 때문에 정답은 5가 됩니다.
n = int(input())
arr = list(map(int,input().split()))

arr.sort()  # 오름차순 정렬

ans = 0
for i in range(n):
    if ans+1 < arr[i]:  # 현재순서까지 추의 합+1이 다음순서 큰 추보다 작으면
        break
 
    ans += arr[i]       

print(ans + 1)

