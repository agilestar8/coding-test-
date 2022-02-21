def solution(dartResult):

    arr = []
    temp = ""
    for i in dartResult:
        if i.isdigit():
            temp += i
            
        elif i == 'S':
            a = int(temp)**1
            arr.append(a)
            temp = ""
            
        elif i == 'D':
            a = int(temp)**2
            arr.append(a)
            temp = ""
            
        elif i == 'T':
            a = int(temp)**3
            arr.append(a)
            temp = ""
            
        elif i == '#':
            arr[-1] = -arr[-1]
            
        elif i == '*':
            arr[-1] = arr[-1]*2
            if len(arr) > 1:
                arr[-2] = arr[-2]*2
                
    return sum(arr)