def solution(dartResult):
    answer = 0
    n = len(dartResult)
    dartResult = list(dartResult)

    # str을 list로
    arr = []
    temp = ""
    for i in dartResult:
        if i.isalpha():
            if len(temp) > 0:
                arr.append(temp)
                arr.append(i)
                temp = ""
            else:
                arr.append(i)

        elif i.isdigit():
            temp += i
        else:
            arr.append(i)
            
    print(arr)

    # 숫자만 stack에 넣기
    stack = []
    for i in range(len(arr)):
        if arr[i] == 'S':
            stack.append(int(arr[i-1])) # ^1배
                    
        elif arr[i] == 'D':
            stack.append(int(arr[i-1])**2) # ^2배
        
        elif arr[i] == 'T':
            stack.append(int(arr[i-1])**3) # ^3배
    
        elif arr[i] == '*': # 맨뒤에서 2개 2배
            stack[-1] = stack[-1]*2
            if len(stack) > 1:            
                stack[-2] = stack[-2]*2
        
        elif arr[i] == '#': # 현재숫자 -1
            stack[-1] = -stack[-1]
            
    print(stack)
    print(sum(stack))
    return (sum(stack))