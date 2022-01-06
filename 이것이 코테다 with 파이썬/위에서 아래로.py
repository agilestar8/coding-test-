n = int(input())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

arr.sort(reverse=True)
for i in arr:
    print(i, end= " ")
