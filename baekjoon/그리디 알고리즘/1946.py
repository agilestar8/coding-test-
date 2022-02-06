import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    info = []
    for _ in range(n):
        a,b = map(int,input().split())
        info.append([a,b])

    info.sort(key = lambda x : x[0])
    print(info)
    temp = info[0][1]   # a과목 1등의 b과목 성적
    ans = 1 # a성적 1등은 통과해두고

    for i in range(1,n):    # a성적 1등 제외하고
        if temp > info[i][1]:    # a성적1등보다 b성적이 좋다면
            ans += 1         # 통과
            temp = info[i][1]     # 더 좋은 성적으로 교체

    print(ans) 


    

