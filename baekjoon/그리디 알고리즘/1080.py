import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = []
b = []
for _ in range(n):
    a.append(list(map(int,input().rstrip())))
for _ in range(n):
    b.append(list(map(int,input().rstrip())))
    
def transform(matrix,x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            matrix[i][j] = 1-matrix[i][j]

    return matrix
     
cnt = 0
for i in range(n-2):        # 012, 123, 234 ... 3개씩 이므로 끝에서 2개전까지 
    for j in range(m-2):     
        if a[i][j] != b[i][j]:
            transform(a,i,j)
            cnt += 1
            
ans = True
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            ans = False

if ans:
    print(cnt)
else:
    print(-1)

