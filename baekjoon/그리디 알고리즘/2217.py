import sys
input = sys.stdin.readline

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
rope.sort()

ans = 0
for i in rope:
    temp = i*n
    if temp > ans:
        ans = temp
    n -= 1

print(ans)
    

        