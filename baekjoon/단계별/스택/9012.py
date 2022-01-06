def check(ps):
    cnt = 0
    for i in ps:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
            if cnt < 0:
                return False
    
    if cnt == 0:
        return True

t = int(input())
for i in range(t):
    ps = input()
    if check(ps):
        print("YES")
    else:
        print("NO")



