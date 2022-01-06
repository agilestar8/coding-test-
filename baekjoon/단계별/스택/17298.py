n = int(input())
arr = list(map(int,input().split()))
stack = []
answer = [-1 for _ in range(n)]

for i in range(n):

    while len(stack)!=0 and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]   # pop을 하면 stack[-1]이 바뀜, 그래서 역순으로 제일큰 것을 전부 왼쪽에 채워넣음
        
    stack.append(i)

print(*answer)
    



