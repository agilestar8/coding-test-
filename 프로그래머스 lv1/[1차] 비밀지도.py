def solution(n, arr1, arr2):
    
    arr = [['0']*n for _ in range(n)]
    # 이진법으로 바꾸기
    for i in range(n):
        temp = ""
        a = bin(arr1[i])[2:]
        for _ in range(n-len(a)):
            temp += '0'
        arr1[i] = temp+a
        
    for i in range(n):
        temp = ""
        a = bin(arr2[i])[2:]
        for _ in range(n-len(a)):
            temp += '0'
        arr2[i] = temp+a

    # 두 지도 겹치기
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                arr[i][j] = '#'
    
    answer = []
    for i in arr:
        a = "".join(i)
        a = a.replace("0"," ")
        answer.append(a)
    
    return answer