n = int(input())
time = list(map(int,input().split()))

for i in range(n):
    time[i] = [time[i],i]

time.sort()
answer = 0
sub = 0
for i in range(n):
    sub += time[i][0]
    answer += sub

print(answer)
