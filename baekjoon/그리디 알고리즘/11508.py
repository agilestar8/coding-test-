import sys
input = sys.stdin.readline

n = int(input())
price = []
for _ in range(n):
    price.append(int(input()))

answer = 0

price.sort(reverse=True)

for i in range(n):
    if (i+1)%3 != 0:
        answer += price[i]
        
print(answer)
