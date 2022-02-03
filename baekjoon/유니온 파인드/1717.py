import sys
input = sys.stdin.readline

# 유니온파인드
# - 공통 원소가 없는 부분 집합들(서로소)로 이루어진 트리 자료구조
# - union과 find를 사용하는 개념

n,m = map(int,input().split())

# 초기화
parent = [-1 for _ in range(n+1)]   # 0제외, 1~n번의 노드 초기화

# Union 
def union(a,b) :    # 노드 두개를 받아서
    a = find(a)     # a의 루트노드 찾기
    b = find(b)     # b의 루트노드 찾기
    
    if a != b :         # 루트노드가 다르면
        parent[b] = a   # b의 루트노드를 a로 변경

# Find
def find(x) :
    if parent[x] < 0:   # x의 루트노드가 0이면 --> (루트노드가 없으면)
        return x        # x자체가 루트노드임
    
    else :              # x의 루트노드가 있다면
        parent[x] = find(parent[x]) # (x의 루트노드)의 루트노드를 찾아서 x의 루트노드로 지정
        return parent[x]            # x의 루트노드 반환

# 입력
for _ in range(m) :
    cmd, a, b = map(int,input().split())
    if cmd == 0:    # 0은 집합 union
        union(a,b)
        
    else:           # 1은 루트 find
        if find(a) == find(b) :     # a와 b의 부모가 같다면
            print("YES")            # 같은 집합임, yes  
        else :                      
            print("NO")
            
            
            