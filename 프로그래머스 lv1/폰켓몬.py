def solution(nums):
    answer = 0
    arr = []

    for i in nums:
        if len(arr) == len(nums) / 2:
            break
        if i not in arr:
            arr.append(i)

    answer = len(arr)
    return answer
