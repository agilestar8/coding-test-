import sys
input = sys.stdin.readline

arr = input().split("-")
arr_sum = []
ans = 0

for i in arr:
    v = i.split("+")
    v = list(map(int,v))
    arr_sum.append(sum(v))

for i in range(1,len(arr_sum)): # 첫번째꺼는 무조건 +
    ans -= arr_sum[i]           # 나머지 합들을 빼줌
    
print(ans + arr_sum[0])         # 첫번째 수 - 나머지합
