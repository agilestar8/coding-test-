import sys,heapq
input = sys.stdin.readline

n = int(input())
meeting = []
for _ in range(n):
    meeting.append(list(map(int,input().split())))

meeting.sort()

q = []
heapq.heappush(q, meeting[0][1])    # 첫 회의 끝나는 시간

for i in range(1,n):            # 다음 회의를
    if q[0] <= meeting[i][0]:   # 이어서 할 수 있으면
        heapq.heappop(q)
        heapq.heappush(q, meeting[i][1])
        
    else:   # 방 추가해야 하면
        heapq.heappush(q, meeting[i][1])

print(len(q))

