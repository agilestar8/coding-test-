# n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 
 
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
 
    return [i for i in range(2, n) if sieve[i] == True]
 
while 1:
    n=int(input())
    if n==0:break
    li=prime_list(2*n+1)
    print(len([i for i in li if i>n]))




