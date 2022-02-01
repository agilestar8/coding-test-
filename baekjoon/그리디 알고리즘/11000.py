import sys,heapq
input = sys.stdin.readline

n = int(input())
lecture = []
for _ in range(n):
    lecture.append(list(map(int,input().split())))

lecture.sort(key = lambda x : x[0]) # lecture에는 가장 빨리 시작하는 강의가 맨 왼쪽

q = []  # 강의실
heapq.heappush(q, lecture[0][1])    # 첫강의 끝나는 시간, 현재 강의실1개

for i in range(1,n):            # 첫 강의 이후

    if lecture[i][0] >= q[0]:   # 뒷강의가 더 늦게 시작하면
        heapq.heappop(q)        # 앞 강의 끝나고
        heapq.heappush(q, lecture[i][1])    # 뒷 강의 이어서 투입
        
    else:                       # 뒷강의랑 시간겹치면
        heapq.heappush(q, lecture[i][1])    #  앞강의 안빼고, 그냥 투입(= 방 추가)
        
print(len(q))   # 현재 강의중인 수
        
    
    
        


