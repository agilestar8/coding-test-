import sys
input = sys.stdin.readline

n,m = map(int,input().split())
j = int(input())
location = []
start = 1
end = m
arr = []
dist = 0

for i in range(j):
    location.append(int(input()))
    
for i in range(j):
    if start > location[i]: # 바구니 왼쪽에 위치하면
        dist += start-location[i]   # 그 차이만큼 이동
        start = location[i]         # 바구니 위치 변경
        end = start+m-1
        
    elif end < location[i]: # 바구니 오른쪽에 위치하면
        dist += location[i]-end
        end = location[i]
        start = end-m+1

print(dist)        
    

        
    
    
    
    
    
    
    

