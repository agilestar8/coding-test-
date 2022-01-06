from collections import deque

t = int(input())
for i in range(t):
    n,m  = map(int,input().split()) # n개 문서, m번째 인덱스의 문서의 출력순서는?
    q = deque(list(map(int,input().split())))
    first_order = deque([0 for _ in range(n)]) # 처음 순서
    first_order[m] = 1  # m번째 마킹
    cnt = 0
    while True:
        if max(q) == q[0]:  # 최대우선순위 = 출력할 차례
            
            if first_order[0] == 1: # 마킹된거 출력할 차례면
                cnt += 1
                print(cnt)
                break
            else:  # 아니면
                q.popleft()  # 그냥 출력
                first_order.popleft()   # 순서에서도 제거
                cnt += 1

        else:   # 출력할 차례 아니면
            q.append(q.popleft())   # 뒤로 보냄
            first_order.append(first_order.popleft())



    


