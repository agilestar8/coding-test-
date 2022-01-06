t = int(input())
for i in range(t):

    command = input()   # 명령
    n = int(input())    # 배열길이
    if n == 0:
        arr = input()
        arr = []
    else:
        arr = list(map(int, input()[1:-1].split(',')))

    error = False        # 에러 - 없음
    is_reverse = False   # 초기화 - 정상상태
    front = 0
    back = 0
    for i in command:
        if i == "R":    # 뒤집는 건 오래 걸리므로 실제 뒤집지 않고, 뒤집혔는지 상태를 변경
            is_reverse = not is_reverse

        elif i == "D":
            if not arr: # 비었으면 에러
                # print("error")
                error = True
                break
            if is_reverse == True:
                back += 1
            else:
                front += 1

    if front+back > len(arr) or error:
        print("error")
    else:
        arr = arr[front:n-back]
        if is_reverse:
            arr.reverse()
            print(str(arr).replace(' ', ''))
        else:
            print(str(arr).replace(' ', ''))
