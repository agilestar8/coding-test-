n, m = map(int,input().split())
arr = list(map(int,input().split()))
# 4 6
# 19 15 10 17

# 0 < h < max(arr) 이므로
start = 0
end = max(arr)
result = 0

while start <= end:
    sum = 0
    mid = (start + end) // 2
    for i in arr:
        if i - mid > 0:
            sum += (i - mid)

    if sum < m:
        end = mid - 1
    elif sum >= m:
        start = mid + 1
        result = mid

print(result)


