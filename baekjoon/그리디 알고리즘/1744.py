import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

pos = []
neg = []
ans = 0

for i in range(n):
    if arr[i] > 1:
        pos.append(arr[i])
    elif arr[i] < 1:
        neg.append(arr[i])
    elif arr[i] == 1:       # 1은 양수지만, 양수끼리 곱하는 거보단 더하는게 이득이므로 따로 처리
        ans += 1

pos.sort(reverse=True)
neg.sort()

# 양수
if len(pos) % 2 == 0:
    for i in range(0,len(pos),2):
        ans += pos[i]*pos[i+1]
else:
    for i in range(0,len(pos)-1,2):
        ans += pos[i]*pos[i+1]
    ans += pos[-1]
            
# 음수, 0
if len(neg) % 2 == 0:
    for i in range(0,len(neg),2):
        ans += neg[i]*neg[i+1]
else:
    for i in range(0,len(neg)-1,2):
        ans += neg[i]*neg[i+1]
    ans += neg[-1]

print(ans)
    


