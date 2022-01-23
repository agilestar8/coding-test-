import sys
input = sys.stdin.readline

i = 1
while True:
    
    l,p,v = map(int,input().split())
    if (l,p,v) == (0,0,0):
        break
    # 캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를 시작했다.
    ans = (v//p)*l      
    ans += min(v%p, l)
    print("Case %d: %d" %(i,ans))
    i += 1
    