from collections import deque

n,m = map(int,input().split())  # 큐 크기, 뽑아낼 수의 개수
idx = list(map(int,input().split()))
q = deque([i for i in range(1,n+1)])
cnt = 0
for i in idx:
    if q.index(i) < len(q)//2 + 1: # 왼쪽에 더 가까우면
        while q[0] != i:
            q.append(q.popleft())   # 왼쪽으로 회전
            cnt += 1         
    else:
        while q[0] != i:
            q.appendleft(q.pop())   # 오른쪽에 가까우면 오른쪽으로 회전
            cnt += 1

    if q[0] == i:
        q.popleft()

# print(q)
print(cnt)





