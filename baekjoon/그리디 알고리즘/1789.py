import sys
input = sys.stdin.readline

# 최소값들로만 더해가다가 S를 넘으면 바로 전의 수가 최대값
s = int(input())

sum = 0
n = 1
while True:   
    sum += n    # 1+2+3+...
    if s < sum:
        break    
    n += 1      # 1,2,3 ..
    
    
print(n-1)  # S를 넘기직전의 n값이 최대값
    
