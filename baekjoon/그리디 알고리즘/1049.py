import sys
input = sys.stdin.readline

n,m = map(int,input().split())
min_a = 1e9
min_b = 1e9

for _ in range(m):
    a,b = map(int,input().split())
    min_a = min(min_a,a)
    min_b = min(min_b,b)
        
# ex) 7개 이상 필요 시, 경우의 수 3가지
price = min(min_a*(n//6+1),             # 패키지로만 구매           6+6
            min_a*(n//6)+min_b*(n%6),   # 패키지 + 단일로 구매      6+1
            min_b*n)                    # 단일로만 구매             7
print(price)
                
            
            
        
        
        
    

    






