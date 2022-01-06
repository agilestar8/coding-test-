# from itertools import combinations
# n,m = map(int,input().split())
# c = combinations(range(1,n+1), m)
# for i in c:
#     print(" ".join(map(str,i)))

n,m = map(int,input().split())
visited = [False]*(n+1)
arr = []

def dfs(cnt,n,m,start):
    if cnt == m:
        print(*arr)

    for i in range(start,n+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)

            dfs(cnt+1,n,m,i+1)  # 고른 수열 오름차순을 위해 i+1부터
            arr.pop()
            visited[i] = False

dfs(0,n,m,1)
