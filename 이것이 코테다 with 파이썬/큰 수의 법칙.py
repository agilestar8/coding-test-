n,m,k = map(int,input().split())

data = list(map(int,input().split()))

data.sort()
one = data[n-1]
two = data[n-2]
total = 0

while True:
    for i in range(k):
        if m == 0:
            break
        total += one
        m -= 1

    if m == 0:
        break

    total += two
    m -= 1

print(total)


 

