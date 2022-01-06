from collections import deque

q = deque()
n = int(input())

for i in range(n,0,-1):
    q.append(i)

while len(q) != 1:

    q.pop()
    q.appendleft(q.pop())

print(q[0])
