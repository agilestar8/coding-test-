import sys
input = sys.stdin.readline

n = int(input())
disc_time = []
for _ in range(n):
    a,b = map(int,input().split())
    disc_time.append([a,b])

# 빨리끝나면서, 빨리시작하는 순서로 정렬
disc_time.sort(key = lambda x : (x[1],x[0]))

ans = 0
end = 0

for i in range(n):
    if disc_time[i][0] >= end:  # 시작시간이 종료시간보다 늦거나 같으면
        end = disc_time[i][1]
        ans += 1
        
print(ans)
  
            




