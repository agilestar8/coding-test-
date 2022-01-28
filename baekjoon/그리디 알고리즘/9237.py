import sys
input = sys.stdin.readline

n = int(input())
tree = list(map(int,input().split()))
time = 0

tree.sort(reverse=True)
arr = []
for idx,day in enumerate(tree):
    arr.append(idx+day+2)   # 심는순서(내림차순 인덱스) + 자라는 시간 + 심는 시간(1) + 이장님오는 다음날(1)

print(max(arr))    
    
    

