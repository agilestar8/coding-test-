import sys 
from bisect import bisect_left

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
DP=[]

# 1. 이분탐색 
# for i in range(N):
#     start=0
#     end=len(DP)-1

#     while start<=end: # A[i]보다 작거나 같은수중에 제일 큰거 위치 찾기
#         mid=(start+end)//2
#         if DP[mid]<A[i]:
#             start=mid+1
#         else:
#             end=mid-1
 
#     if start >= len(DP): # 위치가 배열보다 크다면 넣어준다
#         DP.append(A[i])
#     else: # 해당 위치의 숫자를 바꿔준다.항상 작거나 같은수를 반환하기때문에 비교하지 않아도된다.
#         DP[start]=A[i]

# 2. 이분탐색 bisect
for i in A:
    idx = bisect_left(DP,i)

    if idx >= len(DP):
        DP.append(i)
    else:
        DP[idx] = i

print(len(DP))
 
