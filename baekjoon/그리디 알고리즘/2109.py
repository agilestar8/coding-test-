import sys
input = sys.stdin.readline

n = int(input())
payday = [] # 돈,제한시간
for _ in range(n):
    payday.append(list(map(int,input().split()))) 

print(payday)

payday.sort(key = lambda x : (x[1],-x[0]))  # 빠른기간, 돈많이주는 순
print(payday)

