def solution(n, s):
    answer = []

    # 각 숫자의 차이가 가장 적어야함
    if n > s:
        return [-1]
    
    q,r = divmod(s,n)
    arr = [q]*n    

    idx = 0
    for _ in range(r):
        arr[idx] += 1
        idx += 1
    
    return sorted(arr)