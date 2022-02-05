import sys
input = sys.stdin.readline

g = int(input())    # 게이트 수
p = int(input())    # 비행기 수
arr = [int(input()) for _ in range(p)]  # 도킹할 비행기들

# case2) 유니온 파인드
parent = [i for i in range(g+1)]    # 각 게이트는 자기자신이 루트

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

ans = 0
for i in arr:       # 내가 지금 도킹하려는 게이트를
    p = find(i)     # 루트(최우선)인 p번 게이트에 넣는다

    if p == 0:      # 루트가 0번 == 빈자리가 없다
        break       # break

    ans += 1        # 루트에 넣었다면,
    union(p-1, p)   # p-1번 게이트랑 union == 루트를 왼쪽게이트로 바꿈

print(ans)


# Case 1) 반복문 - 시간초과
# gate = [0]*g
# ans = 0
# havegate = True
# for i in range(p):
#     if havegate:    
#         for j in range(arr[i]-1,-1,-1):   # 뒤에서부터 서치
#             if gate[j] == 0:              # 자리 있으면
#                 gate[j] = 9               # 도킹
#                 ans += 1
#                 break
#             else:                     # 현재 자리 없으면, 앞자리 서치하기전에
#                 if 0 not in gate[:j]: # 전체에서 빈자리가 없으면
#                     havegate = False  # 종료
#                     break     
# print(ans)    