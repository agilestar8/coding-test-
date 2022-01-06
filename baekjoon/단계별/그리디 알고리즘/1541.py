s = input().split("-")
answer = 0
arr = []

for i in s:
    a = i.split("+")
    a = list(map(int,a))
    arr.append(sum(a))

for i in range(1,len(arr)):
    answer -= arr[i]

print(answer+arr[0])