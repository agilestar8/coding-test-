from collections import Counter
def solution(s):

    s = s.replace("{","").replace("}","")
    s = s.split(",")
    s = list(map(int,s))
    
    a = list((Counter(s).items())) # 빈도수 세기
    a.sort(key = lambda x : -x[1]) # 빈도수로 정렬
    
    b = [i for i,j in a] 
    return b

