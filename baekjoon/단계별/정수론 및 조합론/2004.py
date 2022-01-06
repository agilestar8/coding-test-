n,m = map(int,input().split())

# nCm = n! / ((n-m)!*m!)

def div_number(k,num):
    cnt = 0    
    while k!=0:
        k = k//num
        cnt += k
    return cnt
  
div_five = div_number(n, 5) - div_number(m, 5) - div_number(n-m, 5)
div_two = div_number(n, 2) - div_number(m, 2) - div_number(n-m, 2)
print(min(div_five, div_two))
