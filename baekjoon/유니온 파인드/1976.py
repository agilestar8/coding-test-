import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
plan = list(map(int,input().split()))

parent = [-1 for _ in range(n+1)]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[x] = y
        
def find(x):
    if parent[x] < 0:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i+1,j+1)  # 그래프는 i = 0,1,2로 되어있으므로 +1해줘서 1,2,3번으로 표시

answer = []
for i in plan:    
    answer.append(find(i))

if len(set(answer)) == 1: # 루트노드가 다 같으면
    print("YES")
else:                     # 루트노드가 다르면 == 노드가 끊어져있음, 여행 불가
    print("NO")    

