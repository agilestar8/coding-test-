import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    n = int(input())
    stack = list(map(int,input().split()))
    max_price = 0
    profit = 0
        
    for i in range(n-1,-1,-1):
        if max_price < stack[i]:
            max_price = stack[i]

        else:
            profit += max_price-stack[i]
        
    print(profit)

