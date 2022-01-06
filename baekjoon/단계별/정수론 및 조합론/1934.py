t = int(input())

def gcd(a, b):
    if a < b: 
         (a, b) = (b, a) 
     
    while b != 0: 
         (a, b) = (b, a % b) 
      
    return a

for i in range(t):
    a,b = map(int,input().split())
    lcm = a*b//gcd(a,b)
    print(lcm)