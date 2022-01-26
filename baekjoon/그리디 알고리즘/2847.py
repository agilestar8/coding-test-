import sys
input = sys.stdin.readline

n = int(input())
exp = []
for _ in range(n):
    exp.append(int(input()))
cnt = 0

for i in range(n-1, 0, -1): # n-1부터 0까지, -1간격으로
    if exp[i] <= exp[i-1]:  # 이전께 크면
        
        cnt += exp[i-1]-exp[i]+1    # 큰거-작은거 차이만큼에 +1 만큼했을 것
        exp[i-1] = exp[i]-1         # 1만큼 작게 바꾸기
        
        
print(cnt)


