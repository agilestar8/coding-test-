arr = [5,7,9,0,3,1,6,2,4,8]
arr2 = [7,5,9,0,3,1,6,2,4,8]

# 재귀함수로 적용하기 위해서 함수 정의

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:  # pivot보다 큰 값의 인덱스 찾기
            left += 1
        while right > start and arr[right] >= arr[pivot]: # pivot보다 작은 값의 인덱스 찾기
            right -= 1

        if left <= right: # 정상적인 경우
            arr[left],arr[right] = arr[right],arr[left]
        elif left > right: # 엇갈린 경우
            arr[right],arr[pivot] = arr[pivot],arr[right]

    quick_sort(arr, start, end - 1)
    quick_sort(arr, start+1, end)

quick_sort(arr, 0, len(arr)-1)
print(arr)



## 조금 더 쉽고 직관적인 방법
def quick_sort2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0] # pivot
    tail = arr[1:] # pivot 이외의 나머지 리스트

    left_part = [x for x in tail if x <= pivot]  # 나머지 리스트 원소 중에서 pivot보다 작은 값들의 list
    right_part = [x for x in tail if x > pivot]  # 나머지 리스트 원소 중에서 pivot보다 큰 값들의 list

    # 결과적으로 pivot보다 작은 왼쪽파트 / pivot보다 큰 오른쪽파트를 가진 리스트 완성, 이후 재귀적으로 진행
    return quick_sort2(left_part) + [pivot] + quick_sort2(right_part) 
    
print(quick_sort2(arr2))
