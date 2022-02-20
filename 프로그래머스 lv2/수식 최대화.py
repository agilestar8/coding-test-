from itertools import permutations
from copy import deepcopy

def cal(a,b,op):
    if op == "+":
        return str(int(a)+int(b))
    elif op == "-":
        return str(int(a)-int(b))
    elif op == "*":
        return str(int(a)*int(b))
    
def solution(expression):
    op = ["+","-","*"]
    oplist = list(permutations(op,3))
    
    arr = []
    tmp = ""
    for i in expression:
        if i.isdigit()==True: # 숫자면
            tmp += i          # temp에 쓰기

        else:                 # 문자면(연산기호)
            arr.append(tmp)   # 썼던 숫자단위를 arr에 넣기
            arr.append(i)     # 그 다음 연산기호 넣기
            tmp=""            # tmp 초기화
    arr.append(tmp) # 마지막 숫자는 추가안해줬으므로 추가해줘야함

    answer = 0
    for op in oplist:
        arr2 = deepcopy(arr)
        for o in op:
            stack = []
            while arr2:
                temp = arr2.pop(0)
                if temp == o: # 우선순위 연산자면
                    stack.append(cal(stack.pop(),arr2.pop(0),o))
                else: # 그 외(우선순위 떨어지는 연산자, 숫자)는 그대로
                    stack.append(temp)
            arr2 = stack

        answer = max(answer,abs(int(stack[0])))

    return (answer)

print(solution("100-200*300-500+20"))
