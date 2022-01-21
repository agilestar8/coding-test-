import sys
input = sys.stdin.readline

n = int(input())
root = list(map(int,input().split()))
remove_node = int(input())
cnt = 0

# DFS로 제거할 노드의 자식노드 전부 제거
def dfs(v):    
    root[v] = -2            # 부모 간선 제거
    for i in range(n):
        if v == root[i]:    # 제거할 노드가 부모인
            dfs(i)          # 자식들 전부 간선제거
            
dfs(remove_node)

for i in range(n):
    if root[i] != -2 and i not in root: # 제거된 노드가 아니면서, 부모가 아닌 노드면
        cnt += 1    # 리프노드
        
print(cnt)
            

        
   
        
        
    






