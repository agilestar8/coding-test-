from collections import deque

def check(q):
    stack = []
    for i in q:
        if i == "[" or i =="{" or i =="(":
            stack.append(i)      
        else:
            # 닫기가 왔는데, 앞에 열기가 없으면
            if not stack:   
                return False
            # 짝이 안맞으면
            else:
                x = stack.pop()
                if i == ']' and x !='[':    
                    return False
                elif i == '}' and x != '{':
                    return False
                elif i == ')' and x != '(':
                    return False

    # 괄호 열기가 더 많으면(스택에 원소가 남음)
    if stack:
        return False
    else:
        return True

def solution(s):

    s = deque(s)
    l = len(s)
    cnt = 0
    for i in range(l-1):
        if check(s):
            cnt += 1
        s.rotate(-1)

    return cnt
