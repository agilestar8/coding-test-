n,c = map(int,input().split())
home = [int(input()) for _ in range(n)]
home.sort()

start = 1                   # 가장 작은 간격
end = home[-1] - home[0]    # 가장 큰 간격
answer = 0

while start<=end:
    mid = (start+end)//2
    cnt = 1
    prev = home[0]

    for i in range(n):
        if home[i] >= prev + mid:
            cnt += 1
            prev = home[i]

    if cnt >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)

