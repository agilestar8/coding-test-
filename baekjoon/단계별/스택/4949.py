def check(ps):
    stack = []
    for i in ps:
        if i == "(" or i == "[":
            stack.append(i)

        elif i == ")":
            if not stack or stack[-1] == "[":
                return False
            elif "(" == stack[-1]:
                stack.pop()

        elif i == "]":
            if not stack or stack[-1] == "(":
                return False
            elif "[" == stack[-1]:
                stack.pop()
       
    if len(stack) == 0:
        return True
    else:
        return False

while True:
    ps = input()
    if ps == ".":
        break

    if check(ps) == True:
        print("yes")
    else:
        print("no")
