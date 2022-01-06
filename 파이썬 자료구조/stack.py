class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

# 수식 맞는지 체크
def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            S.push(c)

        elif c in match:
            if S.isEmpty():
               return False
        else:
            t = S.pop()
            if t != match[c]:
               return False

        return S.isEmpty()

# 중위 표현식 -> 후위 표현식
prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}
def postfix(S):
    opStack = ArrayStack()
    answer = ''

    for c in S:
        if c == '(':  # 여는 괄호는 스택에 push
            opStack.push(c)
        elif c == ')':  # 닫는 괄호 올 시
            while opStack.peek() != '(':  # 다음 여는 괄호 올때까지
                answer += opStack.pop()
            opStack.pop()  # 스택안의 연산자 pop
        else:  # 그 외에 연산자
            if c in prec:
                if opStack.isEmpty():  # 스택이 비었으면
                    opStack.push(c)  # 연산자 push
                elif prec[opStack.peek()] >= prec[c]:  # 스택의 끝보다 우선순위 낮을 시
                    while not opStack.isEmpty() and prec[opStack.peek()] >= prec[c]:
                        answer += opStack.pop()  # 연산자 pop
                    opStack.push(c)  #
                else:
                    opStack.push(c)
            else:
                answer += c
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer

