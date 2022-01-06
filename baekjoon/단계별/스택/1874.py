n = int(input())
check = True
stack = []
arr = []
cnt = 1
    
for i in range(n):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        arr.append("+")
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        arr.append("-")
    else:
        check = False

if not check:
    print("NO")
else:
    for i in arr:
        print(i)
