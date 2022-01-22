import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# a의 최소 x b의 최대를 반복
ans = 0
for i in range(n):
    
    a_min = a.pop(a.index(min(a)))  # a최소 빼내서
    b_max = b.pop(b.index(max(b)))  # b최대 빼내서
    ans += a_min * b_max            # 곱한값 누적
    
print(ans)    