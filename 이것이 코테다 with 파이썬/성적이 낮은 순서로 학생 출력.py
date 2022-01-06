n = int(input())
arr = []
for i in range(n):
    a = input().split()
    arr.append((a[0],a[1]))

arr.sort(key = lambda x : x[1])

for i in arr:
    print(i[0], end = " ")