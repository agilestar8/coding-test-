import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

cnt = 0
for i in range(n):
    if k == 0:
        break
    
    if k >= coin[i]:
        a = k // coin[i]
        k = k % coin[i]
        cnt += a
            
print(cnt)
    
        
        
        
    
    