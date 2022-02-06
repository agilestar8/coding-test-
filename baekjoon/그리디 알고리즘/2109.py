import sys,heapq
input = sys.stdin.readline

n = int(input())
payday = [] # 돈,제한시간
for _ in range(n):
    payday.append(list(map(int,input().split()))) 

payday.sort(key = lambda x : x[1])  # 제한시간 순 정렬

q = []  # heapq - 실시간으로 적은비용 강의 빼기위해
for i in range(n):

    heapq.heappush(q, payday[i][0]) # 정렬해놓은, 빨리 가야되는 강의의, 가격부터 넣음
    
    if len(q) > payday[i][1]:       # 강의개수가 제한시간보다 길면, 강의못하므로 pay가 제일적은 강의부터 1개 제거
        heapq.heappop(q)

print(sum(q))


