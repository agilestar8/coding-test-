def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    answer = []
    least = 0
    most = 0
    bonus = 0

    for i in lottos:
        if i in win_nums:
            least += 1

    bonus = lottos.count(0)

    most = bonus + least
    return (rank[most], rank[least])