def gcd(a, b):
    if a < b:   # 큰 수, 작은수 형태로 바꿈
         (a, b) = (b, a) 
    while b != 0:  # 작은수가 0이 될 때까지
         (a, b) = (b, a % b) # 작은거 왼쪽, 큰거나누기작은거 나머지는 오른쪽(나머지가 0될때까지)
    return a

n = int(input())
ring = list(map(int,input().split()))

for i in range(1,n):
    print(ring[0]//gcd(ring[0],ring[i]), end="")
    print("/", end="")
    print(ring[i]//gcd(ring[0],ring[i]))

