n,k = map(int,input().split())
q = [i for i in range(1,n+1)]

del_idx = k-1
answer = []

while True:
    answer.append(q.pop(del_idx))
    if not q:
        break
    del_idx = (del_idx+k-1) % len(q)

print("<", end = "")
for i in answer:
    if answer[-1] == i:
        print(i, end = "")
    else:
        print(i, end=", ")
print(">")