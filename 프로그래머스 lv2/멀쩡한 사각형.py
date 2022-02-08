from math import gcd

def solution(w,h):
    
    return w*h-(w+h-gcd(w,h))
    
    # 사용하지못하는 사각형개수 = w+h-최대공약수
    
