def solution(n, money):
    
    dp = [0]*(n+1)
    dp[0] = 1 # 0원을 주는 경우는 1개(아무것도 안주기)
    
    for coin in money:        
        for i in range(coin,n+1): # 1원으로 1~4원으로 만드는 경우
            # 1원 동전만으로 4원을 만드는 방법의 수 + 1원 동전만으로 (4-2)원을 만드는 방법의 수 로 구할 수 있다.
            dp[i] += dp[i-coin]   
    
    return dp[n]%1000000007
