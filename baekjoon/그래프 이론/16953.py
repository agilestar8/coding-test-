import sys
input = sys.stdin.readline
from collections import deque

a,b = map(int,input().split())

def bfs(a):
    q = deque([(a,1)])
    
    while q:
        n,cnt = q.popleft()

        if n == b:
           return cnt
                
        for i in [n*2, n*10+1]:
            if n*2 <= b:
                q.append((i,cnt+1))
            elif (n*10)+1 <= b:
                q.append((i,cnt+1))
    return -1
       
print(bfs(a))
    


