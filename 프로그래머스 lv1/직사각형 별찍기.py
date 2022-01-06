a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a-1):
        print("*", end="")
    print("*")