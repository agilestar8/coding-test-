import sys,heapq
input = sys.stdin.readline

n,k = map(int,input().split())
tool = list(map(int,input().split()))
multi_tap = []
cnt = 0

for i in range(k):
    if tool[i] in multi_tap:    # 멀티탭에 꽂혀있으면
        continue                # 무시

    elif len(multi_tap) < n:        # 멀티탭 자리 있으면
        multi_tap.append(tool[i])   # 꽂기
        continue
    
    # 멀티탭이 꽉 찼을 때
    idxs = []
    for j in range(n):
        try:     # 다시 사용해야 되면
            idx = tool[i:].index(multi_tap[j]) # 얼마나 이후에 사용하는지의 인덱스 추출
        except:  # 다시 사용 안해도 되면
            idx = 101   # 사용회수 초과, 최우선으로 제거하는 인덱스를 가짐
            
        idxs.append(idx)   # 기록

    outidx = idxs.index(max(idxs))  # 가장 나중에 사용하는 것부터 제거(먼저 사용할 플러그는 놔둠, 그래야 절약) 
    del multi_tap[outidx]       # 제거
    multi_tap.append(tool[i])   # 교체
    cnt += 1                    
    
print(cnt)
        
        
        
    