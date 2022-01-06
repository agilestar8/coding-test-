# 4 ≤ n ≤ 10,000

prime_list = [True]*10001
m = int(10001**0.5)

for i in range(2,m+1):
    if prime_list[i]:
        for j in range(2*i,10001,i):
            prime_list[j] = False    # 소수아님

# prime = [i for i in range(2,10001) if prime_list[i] == True and i >= 2]
# print(prime)

t = int(input())
for i in range(t):
    a = int(input())    # 주어진 수
    b = a // 2          # 주어진 수의 절반
    for j in range(b, 1, -1):   # 절반부터 1까지 -1반복
        if prime_list[a-j] == True and prime_list[j] == True:
            print(j, a - j)
            break

