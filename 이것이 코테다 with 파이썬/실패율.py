def solution(N, stages):
    people = len(stages)
    arr = []
    for i in range(1, N + 1):  # 1~N스테이지

        not_clear = stages.count(i)  # 현재 자신이 있는 스테이지를 못깬 사람의 수
        if people == 0:              # 예외 : 도전하고있는 사람이 없을 경우 divide error
            arr.append((i, 0))
            continue
        fail_rate = not_clear / people  # 실패율 = 현재 도전자 수/도달한 도전자 수

        people -= not_clear  # 스테이지 도전자 수 업데이트
        arr.append((i, fail_rate))

    arr.sort(key=lambda x: -x[1])

    return [i[0] for i in arr]



