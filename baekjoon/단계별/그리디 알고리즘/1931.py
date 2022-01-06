n = int(input())
meeting_time = []
answer = 0

for _ in range(n):
    a,b = map(int,input().split())
    meeting_time.append([a,b])

meeting_time.sort(key = lambda x : (x[1],x[0])) # 회의가 1.빨리끝나면서 2.시작이 빠른 순서로 정렬

end = 0
for i,j in meeting_time:
    if i >= end:
        end = j
        answer += 1

print(answer)
