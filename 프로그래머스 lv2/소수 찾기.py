def conv(num,base):
    t = "0123456789ABCDEF"
    q,r = divmod(num,base)
    return conv(q,base) + t[r] if q else t[r]

def isPrime(number):
    if number in (0, 1): # 소수는 2부터
        return False
    for i in range(2, int(number**0.5)+1): # 약수 개수까지만 확인해도 됨
        if number % i == 0:
            return False
    return True
                        
                
def solution(n, k):
    answer = 0
                           
    new_n = str(conv(n,k))
    a = new_n.split('0')
    b = [i for i in a if i] # 0이 이어진 부분 제거
    b = map(int,b)

    for i in b:
        if isPrime(i):
            answer += 1

    return answer