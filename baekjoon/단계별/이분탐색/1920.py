n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int,input().split()))

for i in range(m):
    start = 0
    end = n-1   
    find = False
    while start <= end:
        mid = (start+end)//2
        if arr2[i] == arr[mid]:
            find = True
            break
            
        elif arr2[i] > arr[mid]:
            start = mid+1

        elif arr2[i] < arr[mid]:
            end = mid-1
    
    if find:
        print(1)
    else:
        print(0)
        




