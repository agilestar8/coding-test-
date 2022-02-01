import sys
input = sys.stdin.readline

n,k = map(int,input().split())
tool = list(map(int,input().split()))
multi_tap = []
cnt = 0

for i in range(k):
    if tool[i] in multi_tap:    # 멀티탭에 꽂혀있으면
        continue                # 무시

    elif len(multi_tap) < n:    # 멀티탭 자리 있으면
        multi_tap.append(tool[i])   # 꽂기
        continue
    
    out = 0     # 뽑을 플러그
    outidx = 0  # 뽑은 이후, 몇번째에 사용되는지
    for j in range(n):
        try:                     # 뒤에서 또 사용된다면,
            idx = tool[i:].index(multi_tap[j]) 
            if idx > outidx:    
                out = j         # 인덱스 저장해뒀다가 
                outidx = idx    # 이후에 또 사용할 인덱스

        except:                 # 이후 사용안되면,
            out = j             # 인덱스 저장해서
            break               # 나가서 바로 뽑음
        
    multi_tap[out] = tool[i]    # 뽑을 자리엔 현재도구를 꽂는다
    cnt += 1                    # 하나 뽑았음
    
print(cnt)
        
        
        
        
    