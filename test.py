import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
    
unsati_score = 0
    
print(a)
b = sorted(a)


for i in range(n):
    unsati_score += abs(b[i]-(i+1))
    
print(unsati_score)
    
