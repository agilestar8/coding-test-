import sys
input = sys.stdin.readline

def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        root[b] = a
    
def find(a):
    if root[a] == a:
        return a
    else:
        root[a] = find(root[a])
        return root[a]

v,e = map(int,input().split())
root = [i for i in range(v+1)]

graph = []
for _ in range(e):
    a,b,w = map(int,input().split())
    graph.append((w,a,b))   # a에서 b로 가는 가중치 w
    
graph.sort(key = lambda x : x[0]) # 가중치 적은 순으로 정렬해서 연결 시작하기

ans = 0 # 가중치의 합
for w,a,b in graph:      
    if find(a)!=find(b):    # a와b의 루트비교해보고 (연결되있는지 확인해보고)
        union(a,b)          # 연결안되있으면 연결
        ans += w            # 가중치 더해주기 (위에서 정렬해놨으므로 최소가중치임)
    
print(ans)
    

