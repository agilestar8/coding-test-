# 해당숫자가 소수인지 확인
def isPrime(number):
    if number in [0,1]:     # 0이나 1은 
        return False        # 소수가 아님, 종료
    
    for i in range(2,int(number**0.5)+1):   # 2부터 약수의 개수까지 나눠보기
        if number % i == 0:                 # 1과 자신외에 약수가 있다면
            return False                    # 소수 아님, 종료
        
    return True # 통과했다면, 소수
    
print(isPrime(23))       # 소수
print(isPrime(12375423)) # 소수 아님