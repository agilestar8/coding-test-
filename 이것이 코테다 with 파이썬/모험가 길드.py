n = int(input())
arr = list(map(int,input().split()))
# 5
# 2 3 1 2 2
arr.sort()
cnt = 0
result = 0

for i in arr:
    cnt += 1
    if i <= cnt:
        result += 1
        cnt = 0

print(result)