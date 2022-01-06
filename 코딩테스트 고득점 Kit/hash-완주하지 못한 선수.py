def solution(participant, completion):
    d = {}

    for x in participant:
        d[x] = d.get(x, 0) + 1  # 참가자 명단에 있을 경우 이름 마다 +1
    for x in completion:
        d[x] -= 1  # 완주자 명단에 있을 경우 이름 마다 -1

    for k, v in d.items():
        if v > 0:  # 0이 아니면 완주 못한 사람
            return k
        