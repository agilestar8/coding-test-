def solution(n, t, m, p):
    answer = ''
    temp = ''
    
    def TN(n, base):
        T = "0123456789ABCDEF"
        q, r = divmod(n, base)
        return TN(q, base) + T[r] if q else T[r]
                    
    for i in range(m*t):
        temp += TN(i,n)

    for i in range(len(temp)):
        if i%m == p-1:
            answer += temp[i]
        
        if len(answer) == t:
            break
        
    return answer