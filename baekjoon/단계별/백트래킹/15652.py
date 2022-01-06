# from itertools import combinations_with_replacement
# N,M = map(int, input().split())
# arr = combinations_with_replacement(range(1,N+1), M)
# # 중복을 허용하는 조합
# # 비 내림차순
# for case in arr:
#     print(' '.join(map(str, case)))

n,m = map(int,input().split())
arr = []

def dfs(cnt,idx):
    if cnt == m:
        print(*arr)
        return

    for i in range(idx,n+1):
        arr.append(i)
        dfs(cnt+1,i)
        arr.pop()

dfs(0,1)