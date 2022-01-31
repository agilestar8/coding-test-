import sys,heapq
input = sys.stdin.readline

n = int(input())
card = []
for _ in range(n):
    card.append(int(input()))

heapq.heapify(card)

answer = 0
while len(card) != 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    sum = a+b
    answer += sum
    card.append(sum)
    
print(answer)