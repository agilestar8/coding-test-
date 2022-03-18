import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))    
arr.sort()
x = int(input())
cnt = 0
start = 0
end = n-1

while start < end:
    if arr[start] + arr[end] > x:
        end -= 1
    elif arr[start] + arr[end] < x:
        start += 1
    else:
        cnt += 1
        start += 1
        end -= 1
        
print(cnt)