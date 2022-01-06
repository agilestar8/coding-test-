n,m = map(int,input().split())
tree = list(map(int,input().split()))

start = 1
end = max(tree)

while start<=end:
    cut_len = 0
    mid = (start+end)//2

    for i in tree:
        if i > mid:
            cut_len += (i - mid)

    if cut_len >= m:
        start = mid+1
    else:
        end = mid-1
        
print(end)



