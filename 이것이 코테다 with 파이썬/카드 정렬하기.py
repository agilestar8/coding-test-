import heapq

n = int(input())
card = []
for i in range(n):
    card.append(int(input()))
heapq.heapify(card)

result = 0
while len(card) != 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    sum = a + b
    result += sum
    heapq.heappush(card, sum)

print(result)