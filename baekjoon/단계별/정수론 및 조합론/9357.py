t = int(input())

for _ in range(t):
    n = int(input())
    info = []
    for i in range(n):
        cloth, types = input().split()
        info.append(types)

    set_info = list(set(info))

    answer = 1
    for i in set_info:
        answer *= (info.count(i)+1)

    print(answer-1)


