n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
# 10 7
# 1 3 5 7 9 11 13 15 17 19

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        end = mid - 1
        return binary_search(arr, target, start, end)
    elif arr[mid] < target:
        start = mid + 1
        return binary_search(arr, target, start, end)


result = binary_search(arr,target, 0, n-1)
if result == None:
    print("존재하지 않는 원소")
else:
    print(result+1,"번째")





