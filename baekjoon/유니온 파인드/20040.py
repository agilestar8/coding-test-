import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000000)

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

n,m = map(int,input().split())
root = [i for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    
    if find(a) == find(b):
        print(i+1)
        break
    else:
        union(a,b)
    
else:
    print(0)
    
    

