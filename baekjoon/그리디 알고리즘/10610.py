import sys
input = sys.stdin.readline

# 30의 배수 만들 조건
# 1. 모든 수의 합이 3의 배수여야함
# 2. 일의자리는 0이어야 함

n = list(input().rstrip())
n.sort(reverse=True)        # 내림차순으로 뒤집음 --> 일의 자리에 0있나 확인해야함

sum = 0
for i in n:
    sum += int(i)   # 모든 자리 수의 합
    
if sum % 3 != 0 or '0' not in n:    # 3의배수아니거나 or 0이없으면
    print(-1)                       # 30못만듬
else:
    print("".join(n))               # 내림차순 그대로 붙이면 30의 배수

