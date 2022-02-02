import sys
input = sys.stdin.readline

g = int(input())
p = int(input())
arr = [int(input()) for _ in range(p)] 

# case2) 유니온 파인드
parent = [i for i in range(g+1)] 

def find(curr):
    if parent[curr] == curr:
        return curr
    parent[curr] = find(parent[curr])
    return parent[curr]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

ans = 0
for g in arr:
    p = find(g) # 내가 지금 도킹하려는 게이트
    if p == 0:
        break
    ans += 1
    union(p-1, p) # 이전 게이트랑 union

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