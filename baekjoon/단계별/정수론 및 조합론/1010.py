from math import factorial
# 조합 = mCn 구하기, 순서없이 m개중에 n개를 고르기

t = int(input())

for i in range(t):
    n,m = map(int,input().split())
    answer = factorial(m) // (factorial(n) * factorial(m-n))
    print(answer)

