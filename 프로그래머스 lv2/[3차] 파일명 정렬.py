def solution(files):
    
    arr = []
    for file in files: # 전체 파일
        head = ''
        number = ''
        tail = ''
        
        now_num = False
        for i in range(len(file)): # 하나의 파일을 3가지로 분류하기
            if file[i].isdigit(): # 숫자나오면
                number += file[i]
                now_num = True # 한번 숫자가 나오면 그 순간부터 number차례임

            elif not now_num: # 숫자 나온적 없으면 head에 넣기
                head += file[i]
            
            else: # 숫자가 끝나고 문자가 나오면, 그 뒤는 전부 tail임
                tail = file[i:] # 나머지는 tail로 넣고, 중단
                break
                
        arr.append((head,number,tail))  
        
    print(arr)
    
    # 정렬 조건 
    # 1) 대소문자 -> 정렬key에 upper()해서 정렬 가능
    # 2) 01, 1 똑같게 -> 정렬key에 int()해서 똑같게 가능
    arr.sort(key = lambda x : (x[0].upper(),int(x[1])))
    
    answer = ["".join(i) for i in arr]
    print(arr)            
    return answer      