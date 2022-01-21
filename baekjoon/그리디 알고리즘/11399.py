import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int,input().split()))

time.sort() # 빠른순서대로

total = 0
ans = 0

for i in range(n):
    total += time[i]
    ans += total
    
print(ans)
    
    





