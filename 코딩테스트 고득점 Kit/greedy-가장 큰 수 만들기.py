def solution(number, k):
    arr = []
    for idx, num in enumerate(number):

        while len(arr) > 0 and arr[-1] < num and k > 0:
            arr.pop()
            k -= 1
        if k == 0:
            arr += list(number[idx:])
            break
        arr.append(num)

    arr = arr[:-k] if k > 0 else arr
    answer = "".join(arr)
    return answer
