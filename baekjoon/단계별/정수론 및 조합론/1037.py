t = int(input())
n = list(map(int,input().split()))
n.sort()
answer = n[0]*n[-1]
print(answer)
