def solution(s):
    
    str_num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for i,v in enumerate(str_num):
        s = s.replace(v,str(i))

    return int(s)