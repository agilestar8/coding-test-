a,b = map(int,input().split())

# 유클리드 호제법
def gcd(a, b):
    if a < b: 
         (a, b) = (b, a) 
     
    while b != 0: 
         (a, b) = (b, a % b) 
      
    return a

lcm = a*b // gcd(a,b)

print(gcd(a,b))
print(lcm)