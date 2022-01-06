# from itertools import product
# n,m = map(int,input().split())
# arr = list(range(1,n+1))
# for i in product(arr, repeat=m):
#     print(" ".join(map(str,i)))

n,m = map(int,input().split())
arr = []

def dfs(cnt,n,m):
    if cnt == m:
        print(*arr)
        return

    for i in range(1,n+1):
        arr.append(i)
        dfs(cnt+1,n,m)
        arr.pop()

dfs(0,n,m)

