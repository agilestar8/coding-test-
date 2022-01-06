n = int(input())
arr = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

# 5
# 8 3 7 9 2
# 3
# 5 7 9
arr.sort()

def bsearch(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start+end)//2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start += 1
        elif target < arr[mid]:
            end -= 1
    return None

for i in target:
    result = bsearch(arr,i)
    if result == None:
        print("no", end = " ")
    else:
        print("yes", end = " ")