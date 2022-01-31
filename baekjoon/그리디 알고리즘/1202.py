import sys,heapq
input = sys.stdin.readline

# 가방하나에 보석하나이므로
# --> 작은 가방부터, 넣을 수 있는, 가치 높은 보석부터 채워야함
n,k = map(int,input().split())
gem = []    # 무게,가격 
for _ in range(n):
    gem.append(list(map(int,input().split())))
    
bag = []    # 최대 무게
for _ in range(k):
    bag.append(int(input()))

bag.sort()          # 작은 가방순, 가장 작은 가방부터 채우기
heapq.heapify(gem)  # 작은 보석순, 꺼낼 땐 가장 비싼 순

temp = []
answer = 0
for i in bag:   
    while gem and i >= gem[0][0]:               # 가방에 넣을 수 있는 작은 보석들 중
        print(heapq.heappush(temp, -heapq.heappop(gem)[1]))    # 가장 비싼 것 넣기
        
    if temp:    # 넣었으면
        answer += heapq.heappop(temp)   # 가격 계산

    elif not gem:   
        break

print(-answer)        



    
    
    