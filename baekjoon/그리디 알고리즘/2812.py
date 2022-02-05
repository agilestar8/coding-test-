import sys
input = sys.stdin.readline

n,k = map(int,input().split())
num = list(input().rstrip())
stack = []
idx = n-k

# k개 숫자를 지워서 가장 큰 수 만들기
# - 스택에 맨 앞부터 숫자를 하나씩 넣는다
# - 스택의 맨 뒤에 있는 숫자와 다음으로 넣을 숫자를 비교해서 
# - stack[-1]이 더 작으면 전부 pop(), 다음 수를 stack에 추가
# - stack[-1]이 더 크면 stack에 추가

for i in range(n):
    
    while k > 0 and stack and stack[-1] < num[i]:   # 다음오는 숫자가 stack[-1]보다 작을 때 까지, 스택 다 비우기
        stack.pop()
        k -=1
        
    stack.append(num[i])

print("".join(stack[:idx]))        
    