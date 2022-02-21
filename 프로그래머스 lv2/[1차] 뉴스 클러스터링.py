from collections import Counter

def solution(str1, str2):
    
    # 대문자로
    str1 = str1.upper()
    str2 = str2.upper()
    
    # 2글자씩 끊기 (숫자,특수문자,공백 제거하면서)
    s1 = []
    s2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            s1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            s2.append(str2[i:i+2])    
    print(s1)
    print(s2)
    
    # 교집합 / 합집합 구하기 Counter이용
    c1 = Counter(s1)
    c2 = Counter(s2)
    inter = list((c1 & c2).elements())
    union = list((c1 | c2).elements())

    # 자카드 유사도 구하기
    if len(inter) == 0 and len(union) == 0: # 
        return 65536
    else:
        jab = len(inter)/len(union)
        
    print(jab)  
    return int(jab*65536)