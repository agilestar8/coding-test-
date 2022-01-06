n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
# 10 7
# 1 3 5 7 9 11 13 15 17 19

def binary_search(arr, target):

    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

result = binary_search(arr, target)
print(result+1)
