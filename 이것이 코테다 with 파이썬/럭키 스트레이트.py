n = input()

sumA = 0
sumB = 0
if len(n)%2 == 0:
    a = n[:len(n)//2]
    b = n[len(n)//2:]

    for i in a:
        sumA += int(i)
    for j in b:
        sumB += int(j)

    if sumA == sumB:
        print("LUCKY")
    else:
        print("READY")

else:
    print("READY")

