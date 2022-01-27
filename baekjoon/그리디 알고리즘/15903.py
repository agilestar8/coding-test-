import sys,heapq
input = sys.stdin.readline

n,m = map(int,input().split())
card = list(map(int,input().split()))

# Method 1
# while m:
#     card.sort()
#     temp = card[0] + card[1]
#     card[0] = temp
#     card[1] = temp
#     m -= 1
    
# print(sum(card))

# Method 2
heapq.heapify(card)

for _ in range(m):
    card1 = heapq.heappop(card)    
    card2 = heapq.heappop(card)
    
    temp = card1 + card2
    heapq.heappush(card, temp)
    heapq.heappush(card, temp)

print(sum(card))