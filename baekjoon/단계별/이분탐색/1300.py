n = int(input())
k = int(input())

start = 1
end = k

while start<=end:
    mid = (start+end)//2

    below = 0
    for i in range(1,n+1):
        below += min(n, mid//i)

    if below >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
# 1 2 3  4  
# 2 4 6  8
# 3 6 9  12
# 4 8 12 20

# 6이하 = 10개
# -> 6//4 + 6//3 + 6//2 + 6//1 = 1+2+3+6 = 10
# 8이하 = 12개
# -> 8//1 + 8//2 + 8//3 + 8//4 = 8+4+2+2 = 16이지만, 8은 열의 개수 초과이므로 4로 바꿈
#                              = 4+4+2+2 = 12개 이다

